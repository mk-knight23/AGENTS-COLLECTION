# Deployment Workflow Templates

> Blue-green, canary, rolling, and GitOps deployment strategies with rollback plans.

---

## 1. Blue-Green Deployment

### Strategy
```
                    ┌──────────────┐
                    │  Load Balancer│
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              ▼                         ▼
      ┌───────────────┐        ┌───────────────┐
      │  BLUE (live)  │        │ GREEN (idle)   │
      │  v1.2.0       │        │  v1.3.0        │
      │  ✅ serving   │        │  🔄 deploying  │
      └───────────────┘        └───────────────┘

Step 1: Deploy v1.3.0 to GREEN
Step 2: Run health checks + smoke tests on GREEN
Step 3: Switch load balancer from BLUE → GREEN
Step 4: GREEN is now live, BLUE is idle (instant rollback target)
Step 5: After validation, tear down old BLUE or keep as rollback
```

### GitHub Actions — Blue-Green
```yaml
name: Blue-Green Deploy

on:
  workflow_dispatch:
    inputs:
      environment:
        type: choice
        options: [staging, production]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    steps:
      - uses: actions/checkout@v4

      - name: Determine active slot
        id: slot
        run: |
          ACTIVE=$(aws elbv2 describe-target-groups \
            --names "app-blue" --query 'TargetGroups[0].TargetGroupArn' --output text 2>/dev/null)
          if [ "$ACTIVE" = "blue" ]; then
            echo "deploy_to=green" >> $GITHUB_OUTPUT
            echo "current=blue" >> $GITHUB_OUTPUT
          else
            echo "deploy_to=blue" >> $GITHUB_OUTPUT
            echo "current=green" >> $GITHUB_OUTPUT
          fi

      - name: Deploy to inactive slot
        run: |
          echo "Deploying to ${{ steps.slot.outputs.deploy_to }}"
          # Deploy new version to inactive target group
          aws ecs update-service \
            --cluster app-cluster \
            --service app-${{ steps.slot.outputs.deploy_to }} \
            --task-definition app:latest \
            --desired-count 3

      - name: Wait for healthy
        run: |
          aws ecs wait services-stable \
            --cluster app-cluster \
            --services app-${{ steps.slot.outputs.deploy_to }}

      - name: Smoke test
        run: |
          ENDPOINT="https://${{ steps.slot.outputs.deploy_to }}.internal.example.com"
          for i in {1..5}; do
            STATUS=$(curl -sf -o /dev/null -w "%{http_code}" "$ENDPOINT/health")
            if [ "$STATUS" = "200" ]; then echo "Health check passed"; break; fi
            sleep 5
          done
          [ "$STATUS" = "200" ] || exit 1

      - name: Switch traffic
        run: |
          echo "Switching traffic to ${{ steps.slot.outputs.deploy_to }}"
          # Update ALB listener to point to new target group
          aws elbv2 modify-listener \
            --listener-arn ${{ vars.LISTENER_ARN }} \
            --default-actions Type=forward,TargetGroupArn=${{ steps.slot.outputs.deploy_to == 'blue' && vars.BLUE_TG_ARN || vars.GREEN_TG_ARN }}

      - name: Verify production
        run: |
          sleep 10
          curl -sf https://example.com/health || exit 1
          echo "Deployment verified"

  rollback:
    runs-on: ubuntu-latest
    needs: deploy
    if: failure()
    steps:
      - name: Rollback to previous slot
        run: |
          echo "Rolling back — switching traffic to previous slot"
          # Revert listener to old target group
```

---

## 2. Canary Deployment

### Strategy
```
Traffic Distribution:
  Phase 1:  5% canary  → 95% stable   (5 minutes, watch errors)
  Phase 2: 25% canary  → 75% stable   (10 minutes, watch latency)
  Phase 3: 50% canary  → 50% stable   (15 minutes, watch all metrics)
  Phase 4: 100% canary → 0% stable    (fully promoted)

Auto-rollback triggers:
  - Error rate > 1% (baseline + 0.5%)
  - P99 latency > 500ms (baseline + 100ms)
  - 5xx responses > 0.5%
  - Health check failures > 0
```

### Kubernetes — Argo Rollouts Canary
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: app-rollout
spec:
  replicas: 10
  strategy:
    canary:
      canaryService: app-canary
      stableService: app-stable
      trafficRouting:
        nginx:
          stableIngress: app-ingress
      steps:
        - setWeight: 5
        - pause: { duration: 5m }
        - analysis:
            templates:
              - templateName: error-rate-check
            args:
              - name: service
                value: app-canary
        - setWeight: 25
        - pause: { duration: 10m }
        - analysis:
            templates:
              - templateName: latency-check
        - setWeight: 50
        - pause: { duration: 15m }
        - analysis:
            templates:
              - templateName: full-analysis
        - setWeight: 100
      rollbackWindow:
        revisions: 3
      abortScaleDownDelaySeconds: 30

  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: app
          image: ghcr.io/myorg/app:latest
          ports:
            - containerPort: 8080
          readinessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 10
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 512Mi

---
apiVersion: argoproj.io/v1alpha1
kind: AnalysisTemplate
metadata:
  name: error-rate-check
spec:
  args:
    - name: service
  metrics:
    - name: error-rate
      interval: 60s
      count: 5
      successCondition: result[0] < 0.01
      failureLimit: 2
      provider:
        prometheus:
          address: http://prometheus:9090
          query: |
            sum(rate(http_requests_total{service="{{args.service}}",status=~"5.."}[2m]))
            /
            sum(rate(http_requests_total{service="{{args.service}}"}[2m]))
```

---

## 3. Rolling Deployment

### Kubernetes Rolling Update
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  replicas: 6
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 2          # Max pods over desired count during update
      maxUnavailable: 1    # Max pods unavailable during update
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      terminationGracePeriodSeconds: 60
      containers:
        - name: app
          image: ghcr.io/myorg/app:v1.3.0
          ports:
            - containerPort: 8080
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
            failureThreshold: 3
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 30
            periodSeconds: 15
          lifecycle:
            preStop:
              exec:
                command: ["/bin/sh", "-c", "sleep 10"]
```

---

## 4. GitOps — ArgoCD Application

### argocd-app.yaml
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/k8s-manifests.git
    targetRevision: main
    path: environments/production
    kustomize:
      images:
        - ghcr.io/myorg/app:v1.3.0
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
      - PruneLast=true
      - ApplyOutOfSyncOnly=true
    retry:
      limit: 3
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
  revisionHistoryLimit: 5
```

---

## 5. Rollback Procedures

### Immediate Rollback Script
```bash
#!/bin/bash
set -euo pipefail

APP="${1:?Usage: rollback.sh <app-name> [revision]}"
REVISION="${2:-}"
NAMESPACE="${NAMESPACE:-production}"

echo "╔══════════════════════════════════════╗"
echo "║        EMERGENCY ROLLBACK            ║"
echo "╚══════════════════════════════════════╝"
echo "App:       $APP"
echo "Namespace: $NAMESPACE"

# Kubernetes rollback
if [ -n "$REVISION" ]; then
  echo "Rolling back to revision $REVISION..."
  kubectl rollout undo deployment/"$APP" -n "$NAMESPACE" --to-revision="$REVISION"
else
  echo "Rolling back to previous revision..."
  kubectl rollout undo deployment/"$APP" -n "$NAMESPACE"
fi

# Wait for rollout
echo "Waiting for rollback to complete..."
kubectl rollout status deployment/"$APP" -n "$NAMESPACE" --timeout=300s

# Verify
READY=$(kubectl get deployment "$APP" -n "$NAMESPACE" -o jsonpath='{.status.readyReplicas}')
DESIRED=$(kubectl get deployment "$APP" -n "$NAMESPACE" -o jsonpath='{.spec.replicas}')

if [ "$READY" = "$DESIRED" ]; then
  echo "✅ Rollback successful: $READY/$DESIRED pods ready"
else
  echo "❌ Rollback issue: $READY/$DESIRED pods ready"
  kubectl get pods -n "$NAMESPACE" -l "app=$APP" --sort-by=.metadata.creationTimestamp
  exit 1
fi

# Show current version
IMAGE=$(kubectl get deployment "$APP" -n "$NAMESPACE" \
  -o jsonpath='{.spec.template.spec.containers[0].image}')
echo "Current image: $IMAGE"
echo "Rollback history:"
kubectl rollout history deployment/"$APP" -n "$NAMESPACE" | tail -5
```

---

## 6. Deployment Checklist

```markdown
## Pre-Deployment
- [ ] All tests passing in CI
- [ ] Security scan clean (no CRITICAL/HIGH)
- [ ] Database migrations tested
- [ ] Feature flags configured
- [ ] Monitoring dashboards ready
- [ ] Runbook updated
- [ ] Team notified in #deployments channel

## During Deployment
- [ ] Deploy to staging first
- [ ] Run smoke tests on staging
- [ ] Verify metrics (error rate, latency, throughput)
- [ ] Deploy to production (canary or blue-green)
- [ ] Monitor canary metrics for 15 minutes
- [ ] Promote or rollback based on metrics

## Post-Deployment
- [ ] Verify production health
- [ ] Check error tracking (Sentry)
- [ ] Verify key user flows manually
- [ ] Update deployment log
- [ ] Close related tickets
- [ ] Post in #deployments with summary
```
