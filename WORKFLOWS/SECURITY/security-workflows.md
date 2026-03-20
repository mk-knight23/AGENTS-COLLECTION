# Security Workflow Templates

> SAST, DAST, SCA, and comprehensive DevSecOps pipeline configurations.

---

## 1. Full DevSecOps Pipeline — GitHub Actions

### .github/workflows/security.yml
```yaml
name: Security Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 6 * * 1'  # Weekly Monday 6AM UTC

permissions:
  contents: read
  security-events: write
  actions: read

jobs:
  # ─── SECRET DETECTION ────────────────────────
  secrets:
    name: Secret Scanning
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Gitleaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: TruffleHog
        uses: trufflesecurity/trufflehog@main
        with:
          extra_args: --only-verified --results=verified

  # ─── SAST (Static Analysis) ──────────────────
  sast:
    name: Static Analysis
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Semgrep
        uses: semgrep/semgrep-action@v1
        with:
          config: >-
            p/owasp-top-ten
            p/cwe-top-25
            p/r2c-security-audit
            p/secrets
        env:
          SEMGREP_APP_TOKEN: ${{ secrets.SEMGREP_APP_TOKEN }}

      - name: CodeQL Analysis
        uses: github/codeql-action/init@v3
        with:
          languages: javascript,python

      - name: Autobuild
        uses: github/codeql-action/autobuild@v3

      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v3
        with:
          category: "/language:javascript"

  # ─── SCA (Dependency Scanning) ────────────────
  dependencies:
    name: Dependency Audit
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Node.js dependencies
        if: hashFiles('package-lock.json') != ''
        run: |
          npm ci
          npm audit --production --audit-level=high 2>&1 | tee npm-audit.txt
          npx better-npm-audit audit --level high

      - name: Python dependencies
        if: hashFiles('requirements.txt') != '' || hashFiles('pyproject.toml') != ''
        run: |
          pip install pip-audit safety
          pip-audit --strict --desc 2>&1 | tee pip-audit.txt
          safety check 2>&1 | tee safety-report.txt

      - name: Go dependencies
        if: hashFiles('go.sum') != ''
        run: |
          go install golang.org/x/vuln/cmd/govulncheck@latest
          govulncheck ./... 2>&1 | tee go-vuln.txt

      - name: Trivy filesystem scan
        uses: aquasecurity/trivy-action@0.28.0
        with:
          scan-type: fs
          severity: CRITICAL,HIGH
          exit-code: 1
          format: sarif
          output: trivy-fs.sarif

      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: trivy-fs.sarif

  # ─── CONTAINER SCANNING ──────────────────────
  container:
    name: Container Security
    runs-on: ubuntu-latest
    if: hashFiles('Dockerfile') != ''
    steps:
      - uses: actions/checkout@v4

      - name: Build image
        run: docker build -t test-image:${{ github.sha }} .

      - name: Trivy container scan
        uses: aquasecurity/trivy-action@0.28.0
        with:
          image-ref: test-image:${{ github.sha }}
          severity: CRITICAL,HIGH
          exit-code: 1
          format: sarif
          output: trivy-image.sarif

      - name: Hadolint
        uses: hadolint/hadolint-action@v3.1.0
        with:
          dockerfile: Dockerfile
          failure-threshold: error

      - name: Dockle (CIS Benchmark)
        uses: erzz/dockle-action@v1
        with:
          image: test-image:${{ github.sha }}
          exit-code: 1
          failure-threshold: FATAL

  # ─── IaC SCANNING ────────────────────────────
  iac:
    name: Infrastructure as Code
    runs-on: ubuntu-latest
    if: hashFiles('terraform/**') != '' || hashFiles('k8s/**') != ''
    steps:
      - uses: actions/checkout@v4

      - name: Checkov
        uses: bridgecrewio/checkov-action@master
        with:
          directory: .
          framework: terraform,kubernetes,dockerfile,github_actions
          output_format: sarif
          output_file_path: checkov.sarif
          soft_fail: false

      - name: Trivy IaC scan
        uses: aquasecurity/trivy-action@0.28.0
        with:
          scan-type: config
          severity: CRITICAL,HIGH
          exit-code: 1

      - name: tfsec
        if: hashFiles('terraform/**') != ''
        uses: aquasecurity/tfsec-action@v1.0.3
        with:
          working-directory: terraform/

  # ─── DAST (Dynamic Analysis) ──────────────────
  dast:
    name: Dynamic Analysis
    runs-on: ubuntu-latest
    needs: [sast, dependencies]
    if: github.event_name == 'schedule' || github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4

      - name: Start application
        run: |
          docker compose up -d
          sleep 30
          curl -sf http://localhost:3000/health || exit 1

      - name: ZAP Baseline Scan
        uses: zaproxy/action-baseline@v0.14.0
        with:
          target: http://localhost:3000
          rules_file_name: .zap-rules.tsv
          cmd_options: '-a -j'

      - name: ZAP API Scan
        if: hashFiles('openapi.json') != '' || hashFiles('openapi.yaml') != ''
        uses: zaproxy/action-api-scan@v0.9.0
        with:
          target: http://localhost:3000/openapi.json
          format: openapi

      - name: Cleanup
        if: always()
        run: docker compose down -v

  # ─── LICENSE COMPLIANCE ──────────────────────
  licenses:
    name: License Check
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check licenses
        run: |
          if [ -f "package.json" ]; then
            npm ci
            npx license-checker --production --onlyAllow \
              "MIT;Apache-2.0;BSD-2-Clause;BSD-3-Clause;ISC;0BSD;CC0-1.0;Unlicense;Python-2.0;BlueOak-1.0.0" \
              --excludePrivatePackages
          fi

  # ─── SBOM GENERATION ─────────────────────────
  sbom:
    name: Generate SBOM
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4

      - name: Generate SBOM
        uses: anchore/sbom-action@v0
        with:
          format: spdx-json
          output-file: sbom.spdx.json

      - name: Upload SBOM
        uses: actions/upload-artifact@v4
        with:
          name: sbom-${{ github.sha }}
          path: sbom.spdx.json

  # ─── SECURITY SUMMARY ────────────────────────
  summary:
    name: Security Summary
    runs-on: ubuntu-latest
    needs: [secrets, sast, dependencies, container, iac, licenses]
    if: always()
    steps:
      - name: Check results
        run: |
          echo "## Security Pipeline Results" >> $GITHUB_STEP_SUMMARY
          echo "" >> $GITHUB_STEP_SUMMARY
          echo "| Check | Status |" >> $GITHUB_STEP_SUMMARY
          echo "|-------|--------|" >> $GITHUB_STEP_SUMMARY
          echo "| Secrets | ${{ needs.secrets.result }} |" >> $GITHUB_STEP_SUMMARY
          echo "| SAST | ${{ needs.sast.result }} |" >> $GITHUB_STEP_SUMMARY
          echo "| Dependencies | ${{ needs.dependencies.result }} |" >> $GITHUB_STEP_SUMMARY
          echo "| Containers | ${{ needs.container.result }} |" >> $GITHUB_STEP_SUMMARY
          echo "| IaC | ${{ needs.iac.result }} |" >> $GITHUB_STEP_SUMMARY
          echo "| Licenses | ${{ needs.licenses.result }} |" >> $GITHUB_STEP_SUMMARY
```

---

## 2. Security Gate — PR Check

### .github/workflows/security-gate.yml
```yaml
name: Security Gate

on:
  pull_request:
    branches: [main]

jobs:
  security-gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check for secrets in diff
        run: |
          git diff origin/main...HEAD | grep -iE \
            '(password|secret|api.?key|token|credential)\s*[:=]\s*["\x27][^\s"]{8,}' \
            && echo "::error::Possible secret in diff" && exit 1 || true

      - name: Check security-sensitive files
        run: |
          SENSITIVE_FILES=$(git diff --name-only origin/main...HEAD | grep -E \
            '(auth|security|crypto|session|password|token|key|cert|ssl|tls|\.env|secret)' || true)
          if [ -n "$SENSITIVE_FILES" ]; then
            echo "::warning::Security-sensitive files modified:"
            echo "$SENSITIVE_FILES"
            echo ""
            echo "Requesting security review..."
          fi

      - name: Quick SAST
        run: |
          pip install semgrep
          semgrep --config auto --error \
            --include "$(git diff --name-only origin/main...HEAD | tr '\n' ',')" \
            . 2>/dev/null || true

      - name: Dependency delta check
        run: |
          if git diff origin/main...HEAD --name-only | grep -qE '(package-lock|requirements|go\.sum|Cargo\.lock)'; then
            echo "::notice::Dependency files changed — running audit"
            if [ -f "package-lock.json" ]; then
              npm ci && npm audit --production --audit-level=high
            fi
          fi
```

---

## 3. Incident Response Workflow

### .github/workflows/incident-response.yml
```yaml
name: Security Incident Response

on:
  workflow_dispatch:
    inputs:
      severity:
        description: 'Incident severity'
        required: true
        type: choice
        options: [critical, high, medium, low]
      description:
        description: 'Brief description'
        required: true

jobs:
  triage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Create incident issue
        uses: actions/github-script@v7
        with:
          script: |
            const issue = await github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: `[SECURITY-${{ inputs.severity  }}] ${{ inputs.description }}`,
              body: `## Security Incident Report

              **Severity:** ${{ inputs.severity }}
              **Reported:** ${new Date().toISOString()}
              **Reporter:** ${context.actor}

              ## Description
              ${{ inputs.description }}

              ## Checklist
              - [ ] Incident confirmed
              - [ ] Impact assessed
              - [ ] Containment actions taken
              - [ ] Root cause identified
              - [ ] Fix implemented
              - [ ] Fix verified
              - [ ] Post-mortem scheduled
              - [ ] Lessons learned documented
              `,
              labels: ['security', 'incident', '${{ inputs.severity }}'],
              assignees: [context.actor]
            });
            core.setOutput('issue_number', issue.data.number);

      - name: Run emergency scan
        if: inputs.severity == 'critical'
        run: |
          echo "Running emergency security scan..."
          pip install semgrep
          semgrep --config auto --json -o emergency-scan.json . || true

      - name: Notify team
        run: |
          echo "::error::SECURITY INCIDENT [${{ inputs.severity }}]: ${{ inputs.description }}"
```

---

## 4. Vulnerability Severity Matrix

```
CRITICAL (CVSS 9.0-10.0) — Fix IMMEDIATELY
  • Remote code execution
  • Authentication bypass
  • SQL injection with data exfiltration
  • Hardcoded production credentials
  Timeline: 24 hours

HIGH (CVSS 7.0-8.9) — Fix within 1 sprint
  • XSS (stored)
  • SSRF
  • Privilege escalation
  • Insecure deserialization
  Timeline: 1 week

MEDIUM (CVSS 4.0-6.9) — Schedule fix
  • XSS (reflected)
  • CSRF
  • Missing security headers
  • Information disclosure
  Timeline: 2 weeks

LOW (CVSS 0.1-3.9) — Track and fix when convenient
  • Verbose error messages
  • Missing rate limiting (non-auth)
  • DNS misconfiguration
  • Outdated non-vulnerable dependencies
  Timeline: Next release
```
