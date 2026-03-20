# Security Scanner Configurations

> Ready-to-use configs for SAST, DAST, SCA, secret detection, and container scanning.

---

## 1. Semgrep — Static Analysis (SAST)

### .semgrep.yml
```yaml
rules:
  # SQL Injection
  - id: sql-injection-format-string
    patterns:
      - pattern: |
          $CURSOR.execute(f"...{$VAR}...")
    message: "Possible SQL injection via f-string. Use parameterized queries."
    languages: [python]
    severity: ERROR
    metadata:
      owasp: A03:2021
      cwe: CWE-89

  # XSS Prevention
  - id: react-dangerouslysetinnerhtml
    pattern: dangerouslySetInnerHTML={...}
    message: "dangerouslySetInnerHTML can lead to XSS. Sanitize input with DOMPurify."
    languages: [typescript, javascript]
    severity: WARNING
    metadata:
      owasp: A03:2021
      cwe: CWE-79

  # Hardcoded Secrets
  - id: hardcoded-secret
    patterns:
      - pattern-regex: (?i)(api[_-]?key|secret|password|token)\s*[:=]\s*["'][A-Za-z0-9+/=]{16,}["']
    message: "Possible hardcoded secret. Use environment variables or a secret manager."
    languages: [generic]
    severity: ERROR
    metadata:
      owasp: A02:2021
      cwe: CWE-798

  # Insecure Crypto
  - id: weak-hash-md5
    patterns:
      - pattern: hashlib.md5(...)
      - pattern: crypto.createHash("md5")
    message: "MD5 is cryptographically broken. Use SHA-256 or SHA-3."
    languages: [python, javascript, typescript]
    severity: ERROR
    metadata:
      cwe: CWE-328

  # Path Traversal
  - id: path-traversal
    patterns:
      - pattern: os.path.join($BASE, request.$ATTR)
      - pattern: path.join($BASE, req.params.$ATTR)
    message: "Potential path traversal. Validate and canonicalize paths."
    languages: [python, javascript, typescript]
    severity: ERROR
    metadata:
      owasp: A01:2021
      cwe: CWE-22

  # Command Injection
  - id: command-injection-subprocess
    patterns:
      - pattern: subprocess.call($CMD, shell=True)
      - pattern: subprocess.Popen($CMD, shell=True)
    message: "shell=True enables command injection. Use shell=False with argument list."
    languages: [python]
    severity: ERROR
    metadata:
      owasp: A03:2021
      cwe: CWE-78

  # Insecure Deserialization
  - id: pickle-insecure-deserialization
    patterns:
      - pattern: pickle.loads(...)
      - pattern: pickle.load(...)
    message: "pickle deserialization is unsafe with untrusted data. Use JSON or protobuf."
    languages: [python]
    severity: ERROR
    metadata:
      owasp: A08:2021
      cwe: CWE-502

  # SSRF
  - id: ssrf-user-controlled-url
    patterns:
      - pattern: requests.get($URL)
        metavariable-regex:
          metavariable: $URL
          regex: ".*request.*|.*req\\."
    message: "User-controlled URL in HTTP request. Validate against allowlist."
    languages: [python]
    severity: ERROR
    metadata:
      owasp: A10:2021
      cwe: CWE-918
```

### Run Commands
```bash
# Install
pip install semgrep

# Run with config
semgrep --config .semgrep.yml .

# Run with auto rules (community + pro)
semgrep --config auto .

# CI mode (returns exit code 1 on findings)
semgrep --config auto --error .

# Specific OWASP checks
semgrep --config "p/owasp-top-ten" .

# Language-specific
semgrep --config "p/python" --config "p/typescript" .
```

---

## 2. Gitleaks — Secret Detection

### .gitleaks.toml
```toml
title = "Gitleaks Custom Config"

[extend]
useDefault = true

[[rules]]
id = "custom-api-key"
description = "Custom API key pattern"
regex = '''(?i)(?:api[_-]?key|apikey)\s*[:=]\s*['"]?([A-Za-z0-9_\-]{20,})['"]?'''
entropy = 3.5
secretGroup = 1
tags = ["key", "api"]

[[rules]]
id = "jwt-token"
description = "JWT Token"
regex = '''eyJ[A-Za-z0-9-_]+\.eyJ[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+'''
tags = ["token", "jwt"]

[[rules]]
id = "slack-webhook"
description = "Slack Webhook URL"
regex = '''https://hooks\.slack\.com/services/T[A-Z0-9]+/B[A-Z0-9]+/[A-Za-z0-9]+'''
tags = ["webhook", "slack"]

[[rules]]
id = "stripe-key"
description = "Stripe API Key"
regex = '''(?:sk|pk)_(?:test|live)_[A-Za-z0-9]{20,}'''
tags = ["key", "stripe"]

[[rules]]
id = "sendgrid-key"
description = "SendGrid API Key"
regex = '''SG\.[A-Za-z0-9_\-]{22}\.[A-Za-z0-9_\-]{43}'''
tags = ["key", "sendgrid"]

[allowlist]
paths = [
  '''\.lock$''',
  '''go\.sum$''',
  '''package-lock\.json$''',
  '''yarn\.lock$''',
  '''\.png$''',
  '''\.jpg$''',
  '''\.gif$''',
  '''\.svg$''',
  '''\.woff2?$''',
  '''\.min\.js$''',
  '''\.min\.css$''',
  '''node_modules/''',
  '''vendor/''',
  '''dist/''',
  '''__pycache__/''',
  '''\.env\.example$''',
]
```

### Run Commands
```bash
# Install
brew install gitleaks  # macOS
# or: go install github.com/gitleaks/gitleaks/v8@latest

# Scan repo
gitleaks detect --source . --verbose

# Scan staged changes only (pre-commit)
gitleaks protect --staged --verbose

# With custom config
gitleaks detect --config .gitleaks.toml --source .

# Generate report
gitleaks detect --source . --report-format json --report-path gitleaks-report.json
```

---

## 3. Trivy — Container & Filesystem Scanning

### trivy.yaml
```yaml
# trivy.yaml — project-level config
severity:
  - CRITICAL
  - HIGH

scan:
  skip-dirs:
    - node_modules
    - vendor
    - .git
    - dist
    - __pycache__

  skip-files:
    - "*.test.ts"
    - "*.spec.ts"
    - "*_test.go"

vulnerability:
  type:
    - os
    - library

  ignore-unfixed: true

misconfiguration:
  scanners:
    - dockerfile
    - terraform
    - kubernetes
    - cloudformation

  policy-namespaces:
    - user

secret:
  config: trivy-secret.yaml
```

### Run Commands
```bash
# Install
brew install trivy

# Scan filesystem (dependencies)
trivy fs --severity HIGH,CRITICAL .

# Scan container image
trivy image --severity HIGH,CRITICAL myapp:latest

# Scan Kubernetes manifests
trivy config --severity HIGH,CRITICAL ./k8s/

# Scan Terraform
trivy config --severity HIGH,CRITICAL ./terraform/

# Generate SBOM (Software Bill of Materials)
trivy fs --format spdx-json --output sbom.json .

# CI mode (exit code 1 on findings)
trivy fs --exit-code 1 --severity CRITICAL .
```

---

## 4. OWASP ZAP — Dynamic Analysis (DAST)

### zap-baseline.conf
```conf
# ZAP Baseline scan config
# Rules to IGNORE (false positives)
10015	IGNORE	(Incomplete or No Cache-control)
10037	IGNORE	(Server Leaks via X-Powered-By)
10098	IGNORE	(Cross-Domain Misconfiguration)

# Rules to WARN
10021	WARN	(X-Content-Type-Options Missing)
10036	WARN	(Server Leaks Version Info)

# Rules to FAIL
10038	FAIL	(Content Security Policy Missing)
10049	FAIL	(Storable and Cacheable Content)
40012	FAIL	(Cross Site Scripting Reflected)
40014	FAIL	(Cross Site Scripting Persistent)
40018	FAIL	(SQL Injection)
90033	FAIL	(Loosely Scoped Cookie)
```

### Run Commands
```bash
# Baseline scan (passive only, fast)
docker run -t ghcr.io/zaproxy/zaproxy:stable zap-baseline.py \
  -t https://myapp.com \
  -c zap-baseline.conf \
  -r zap-report.html

# Full scan (passive + active, thorough)
docker run -t ghcr.io/zaproxy/zaproxy:stable zap-full-scan.py \
  -t https://myapp.com \
  -r zap-full-report.html

# API scan (OpenAPI spec)
docker run -t ghcr.io/zaproxy/zaproxy:stable zap-api-scan.py \
  -t https://myapp.com/openapi.json \
  -f openapi \
  -r zap-api-report.html

# GraphQL scan
docker run -t ghcr.io/zaproxy/zaproxy:stable zap-api-scan.py \
  -t https://myapp.com/graphql \
  -f graphql \
  -r zap-graphql-report.html
```

---

## 5. npm audit / pip audit / go vuln — Dependency Scanning

### npm audit config (.npmrc)
```ini
audit=true
audit-level=high
fund=false
```

### Run Commands
```bash
# JavaScript/TypeScript
npm audit --production
npm audit fix
npx better-npm-audit audit --level high

# Python
pip install pip-audit
pip-audit --strict --desc
pip-audit -r requirements.txt --fix

# Go
go install golang.org/x/vuln/cmd/govulncheck@latest
govulncheck ./...

# Ruby
gem install bundler-audit
bundle-audit check --update

# Rust
cargo install cargo-audit
cargo audit
```

---

## 6. Checkov — Infrastructure as Code Security

### .checkov.yml
```yaml
branch: main
compact: true
directory:
  - terraform/
  - k8s/
  - cloudformation/
download-external-modules: true
evaluate-variables: true
framework:
  - terraform
  - kubernetes
  - dockerfile
  - github_actions
output:
  - cli
  - json
quiet: true
skip-check:
  - CKV_AWS_18   # S3 access logging (dev environments)
  - CKV_AWS_144  # S3 cross-region replication (not needed)
soft-fail-on:
  - CKV_AWS_20   # S3 public access (some buckets are public)
```

### Run Commands
```bash
pip install checkov

# Scan Terraform
checkov -d ./terraform/ --config-file .checkov.yml

# Scan Kubernetes
checkov -d ./k8s/ --framework kubernetes

# Scan Dockerfile
checkov -f Dockerfile

# Scan GitHub Actions
checkov -d .github/workflows/ --framework github_actions
```

---

## Master Security Scan Script

```bash
#!/bin/bash
set -euo pipefail

echo "╔══════════════════════════════════════════════╗"
echo "║     FULL SECURITY SCAN — SENTINEL MODE       ║"
echo "╚══════════════════════════════════════════════╝"

REPORT_DIR="./security-reports"
mkdir -p "$REPORT_DIR"
EXIT_CODE=0

# 1. Secret Detection
echo -e "\n[1/6] 🔑 Secret Detection (Gitleaks)..."
if command -v gitleaks &>/dev/null; then
  gitleaks detect --source . --report-format json \
    --report-path "$REPORT_DIR/secrets.json" 2>/dev/null || EXIT_CODE=1
  echo "     → Report: $REPORT_DIR/secrets.json"
else
  echo "     → SKIP: gitleaks not installed"
fi

# 2. SAST (Semgrep)
echo -e "\n[2/6] 🔍 Static Analysis (Semgrep)..."
if command -v semgrep &>/dev/null; then
  semgrep --config auto --json --output "$REPORT_DIR/sast.json" . 2>/dev/null || EXIT_CODE=1
  echo "     → Report: $REPORT_DIR/sast.json"
else
  echo "     → SKIP: semgrep not installed"
fi

# 3. Dependency Vulnerabilities
echo -e "\n[3/6] 📦 Dependency Scan..."
if [ -f "package.json" ]; then
  npm audit --json > "$REPORT_DIR/npm-audit.json" 2>/dev/null || EXIT_CODE=1
  echo "     → npm: $REPORT_DIR/npm-audit.json"
fi
if [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
  pip-audit --format json --output "$REPORT_DIR/pip-audit.json" 2>/dev/null || EXIT_CODE=1
  echo "     → pip: $REPORT_DIR/pip-audit.json"
fi
if [ -f "go.mod" ]; then
  govulncheck -json ./... > "$REPORT_DIR/go-vuln.json" 2>/dev/null || EXIT_CODE=1
  echo "     → go: $REPORT_DIR/go-vuln.json"
fi

# 4. Container Scanning
echo -e "\n[4/6] 🐳 Container Scan (Trivy)..."
if command -v trivy &>/dev/null; then
  trivy fs --severity HIGH,CRITICAL --format json \
    --output "$REPORT_DIR/trivy-fs.json" . 2>/dev/null || EXIT_CODE=1
  echo "     → Report: $REPORT_DIR/trivy-fs.json"
else
  echo "     → SKIP: trivy not installed"
fi

# 5. IaC Scanning
echo -e "\n[5/6] ☁️ IaC Scan (Checkov)..."
if command -v checkov &>/dev/null; then
  if [ -d "terraform" ] || [ -d "k8s" ]; then
    checkov -d . --output json > "$REPORT_DIR/iac.json" 2>/dev/null || EXIT_CODE=1
    echo "     → Report: $REPORT_DIR/iac.json"
  else
    echo "     → SKIP: No IaC files found"
  fi
else
  echo "     → SKIP: checkov not installed"
fi

# 6. License Compliance
echo -e "\n[6/6] ⚖️ License Check..."
if [ -f "package.json" ] && command -v npx &>/dev/null; then
  npx license-checker --json --production \
    > "$REPORT_DIR/licenses.json" 2>/dev/null || true
  echo "     → Report: $REPORT_DIR/licenses.json"
fi

echo ""
echo "═══════════════════════════════════════════════"
if [ $EXIT_CODE -eq 0 ]; then
  echo "✅ ALL SCANS PASSED"
else
  echo "❌ ISSUES FOUND — Review reports in $REPORT_DIR/"
fi
echo "═══════════════════════════════════════════════"

exit $EXIT_CODE
```
