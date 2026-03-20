# CI/CD Workflow Templates

> Production-ready GitHub Actions and GitLab CI templates for every stack.

---

## 1. Universal CI Pipeline — GitHub Actions

### .github/workflows/ci.yml
```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: read
  pull-requests: write
  security-events: write

jobs:
  # ─── DETECT CHANGES ──────────────────────────
  changes:
    runs-on: ubuntu-latest
    outputs:
      backend: ${{ steps.filter.outputs.backend }}
      frontend: ${{ steps.filter.outputs.frontend }}
      infra: ${{ steps.filter.outputs.infra }}
      docs: ${{ steps.filter.outputs.docs }}
    steps:
      - uses: actions/checkout@v4
      - uses: dorny/paths-filter@v3
        id: filter
        with:
          filters: |
            backend:
              - 'src/api/**'
              - 'src/server/**'
              - 'requirements.txt'
              - 'pyproject.toml'
              - 'go.mod'
            frontend:
              - 'src/app/**'
              - 'src/components/**'
              - 'package.json'
            infra:
              - 'terraform/**'
              - 'k8s/**'
              - 'Dockerfile*'
              - 'docker-compose*.yml'
            docs:
              - 'docs/**'
              - '*.md'

  # ─── LINT & FORMAT ───────────────────────────
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Detect language and lint
        run: |
          if [ -f "package.json" ]; then
            npm ci
            npm run lint
            npx tsc --noEmit
          fi
          if [ -f "pyproject.toml" ]; then
            pip install ruff mypy
            ruff check .
            ruff format --check .
          fi
          if [ -f "go.mod" ]; then
            go vet ./...
            curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh
            ./bin/golangci-lint run
          fi

  # ─── TEST ─────────────────────────────────────
  test:
    runs-on: ubuntu-latest
    needs: lint
    strategy:
      matrix:
        shard: [1, 2, 3]
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_DB: test
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
        ports: ['5432:5432']
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
      redis:
        image: redis:7-alpine
        ports: ['6379:6379']
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4

      - name: Run tests with coverage
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test
          REDIS_URL: redis://localhost:6379
          CI: true
        run: |
          if [ -f "package.json" ]; then
            npm ci
            npx vitest run --coverage --shard=${{ matrix.shard }}/3
          elif [ -f "pyproject.toml" ]; then
            pip install -e ".[test]"
            pytest --cov --cov-report=xml -x --splits 3 --group ${{ matrix.shard }}
          elif [ -f "go.mod" ]; then
            go test -v -race -coverprofile=coverage.out ./...
          fi

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          flags: shard-${{ matrix.shard }}

  # ─── BUILD ────────────────────────────────────
  build:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v4

      - name: Build application
        run: |
          if [ -f "package.json" ]; then
            npm ci
            npm run build
          elif [ -f "pyproject.toml" ]; then
            pip install build
            python -m build
          elif [ -f "go.mod" ]; then
            CGO_ENABLED=0 go build -ldflags="-s -w" -o bin/app ./cmd/server
          fi

      - name: Upload build artifact
        uses: actions/upload-artifact@v4
        with:
          name: build-${{ github.sha }}
          path: |
            dist/
            build/
            bin/
          retention-days: 7

  # ─── DOCKER BUILD ─────────────────────────────
  docker:
    runs-on: ubuntu-latest
    needs: [test, build]
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push
        uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: |
            ghcr.io/${{ github.repository }}:${{ github.sha }}
            ghcr.io/${{ github.repository }}:latest
          cache-from: type=gha
          cache-to: type=gha,mode=max
          platforms: linux/amd64,linux/arm64

  # ─── DEPLOY (staging on main) ─────────────────
  deploy-staging:
    runs-on: ubuntu-latest
    needs: docker
    if: github.ref == 'refs/heads/main'
    environment:
      name: staging
      url: https://staging.example.com
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to staging
        run: |
          echo "Deploy ghcr.io/${{ github.repository }}:${{ github.sha }} to staging"
          # kubectl set image deployment/app app=ghcr.io/${{ github.repository }}:${{ github.sha }}
          # or: railway up, fly deploy, vercel --prod, etc.
```

---

## 2. Node.js / TypeScript CI

### .github/workflows/node-ci.yml
```yaml
name: Node.js CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  ci:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [20, 22]

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'

      - run: npm ci
      - run: npx tsc --noEmit
      - run: npm run lint
      - run: npm test -- --coverage
      - run: npm run build

      - name: E2E Tests
        if: matrix.node-version == 22
        run: |
          npx playwright install --with-deps chromium
          npm run test:e2e
```

---

## 3. Python CI

### .github/workflows/python-ci.yml
```yaml
name: Python CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  ci:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.11', '3.12', '3.13']

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install uv
        uses: astral-sh/setup-uv@v4

      - name: Install dependencies
        run: uv sync --frozen

      - name: Lint
        run: |
          uv run ruff check .
          uv run ruff format --check .

      - name: Type check
        run: uv run mypy .

      - name: Test
        run: uv run pytest --cov --cov-report=xml -x

      - name: Security scan
        run: |
          uv run pip-audit
          uv run bandit -r src/
```

---

## 4. Go CI

### .github/workflows/go-ci.yml
```yaml
name: Go CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: '1.23'

      - name: Vet
        run: go vet ./...

      - name: Lint
        uses: golangci/golangci-lint-action@v6
        with:
          version: latest

      - name: Test
        run: go test -v -race -coverprofile=coverage.out ./...

      - name: Build
        run: CGO_ENABLED=0 go build -ldflags="-s -w" -o bin/app ./cmd/server

      - name: Vulnerability check
        run: |
          go install golang.org/x/vuln/cmd/govulncheck@latest
          govulncheck ./...
```

---

## 5. GitLab CI Template

### .gitlab-ci.yml
```yaml
stages:
  - lint
  - test
  - build
  - security
  - deploy

variables:
  DOCKER_TLS_CERTDIR: "/certs"

# ─── TEMPLATES ────────────────────────────────
.node-template: &node-defaults
  image: node:22-slim
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/
  before_script:
    - npm ci

# ─── LINT ─────────────────────────────────────
lint:
  <<: *node-defaults
  stage: lint
  script:
    - npx tsc --noEmit
    - npm run lint
    - npx prettier --check .

# ─── TEST ─────────────────────────────────────
test:
  <<: *node-defaults
  stage: test
  services:
    - postgres:16
    - redis:7-alpine
  variables:
    POSTGRES_DB: test
    POSTGRES_USER: test
    POSTGRES_PASSWORD: test
    DATABASE_URL: postgresql://test:test@postgres:5432/test
    REDIS_URL: redis://redis:6379
  script:
    - npm test -- --coverage
  coverage: /All files[^|]*\|[^|]*\s+([\d\.]+)/
  artifacts:
    reports:
      junit: test-results.xml
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

# ─── BUILD ────────────────────────────────────
build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  only:
    - main

# ─── SECURITY ─────────────────────────────────
sast:
  stage: security
  image: semgrep/semgrep
  script:
    - semgrep --config auto --error --json -o semgrep.json .
  artifacts:
    reports:
      sast: semgrep.json
  allow_failure: true

dependency-scan:
  <<: *node-defaults
  stage: security
  script:
    - npm audit --production --audit-level=high
  allow_failure: true

# ─── DEPLOY ───────────────────────────────────
deploy-staging:
  stage: deploy
  script:
    - echo "Deploying $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA to staging"
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - main

deploy-production:
  stage: deploy
  script:
    - echo "Deploying $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA to production"
  environment:
    name: production
    url: https://example.com
  when: manual
  only:
    - main
```

---

## 6. Monorepo CI (Turborepo / Nx)

### .github/workflows/monorepo-ci.yml
```yaml
name: Monorepo CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Full history for affected detection

      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: 'npm'

      - run: npm ci

      # Turborepo: only build affected packages
      - name: Build affected
        run: npx turbo run build --filter='...[origin/main]'

      - name: Test affected
        run: npx turbo run test --filter='...[origin/main]'

      - name: Lint affected
        run: npx turbo run lint --filter='...[origin/main]'

      # Remote caching
      - name: Turbo cache
        env:
          TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
          TURBO_TEAM: ${{ vars.TURBO_TEAM }}
        run: npx turbo run build test lint --cache-dir=.turbo
```

---

## 7. Release / Versioning

### .github/workflows/release.yml
```yaml
name: Release

on:
  push:
    branches: [main]

permissions:
  contents: write
  packages: write

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      # Semantic Release: auto version + changelog + github release
      - uses: actions/setup-node@v4
        with:
          node-version: 22

      - run: npm ci

      - name: Semantic Release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
        run: npx semantic-release
```

### .releaserc.json
```json
{
  "branches": ["main"],
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/changelog",
    ["@semantic-release/npm", { "npmPublish": false }],
    "@semantic-release/github",
    ["@semantic-release/git", {
      "assets": ["CHANGELOG.md", "package.json"],
      "message": "chore(release): ${nextRelease.version} [skip ci]"
    }]
  ]
}
```
