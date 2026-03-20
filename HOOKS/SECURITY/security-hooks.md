# Security Hooks Collection

> Pre-commit and runtime hooks for automated security enforcement.

---

## Pre-Commit Hooks (.pre-commit-config.yaml)

```yaml
repos:
  # Secret Detection
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.4
    hooks:
      - id: gitleaks

  # TruffleHog - Advanced secret scanning
  - repo: https://github.com/trufflesecurity/trufflehog
    rev: v3.82.6
    hooks:
      - id: trufflehog
        entry: trufflehog git file://. --since-commit HEAD --only-verified --fail

  # Detect AWS credentials
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: detect-aws-credentials
        args: [--allow-missing-credentials]
      - id: detect-private-key
      - id: check-added-large-files
        args: [--maxkb=500]
      - id: check-merge-conflict
      - id: check-yaml
      - id: check-json
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: no-commit-to-branch
        args: [--branch, main, --branch, master]

  # Semgrep - Code security patterns
  - repo: https://github.com/semgrep/semgrep
    rev: v1.90.0
    hooks:
      - id: semgrep
        args: [--config, auto, --error]
        stages: [pre-commit]

  # Bandit - Python security
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.10
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]

  # Safety - Python dependency vulnerability check
  - repo: https://github.com/Lucas-C/pre-commit-hooks-safety
    rev: v1.3.3
    hooks:
      - id: python-safety-dependencies-check

  # Checkov - IaC security scanning
  - repo: https://github.com/bridgecrewio/checkov
    rev: 3.2.255
    hooks:
      - id: checkov
        args: [--framework, terraform]

  # Hadolint - Dockerfile best practices
  - repo: https://github.com/hadolint/hadolint
    rev: v2.12.0
    hooks:
      - id: hadolint

  # ShellCheck - Shell script analysis
  - repo: https://github.com/shellcheck-py/shellcheck-py
    rev: v0.10.0.1
    hooks:
      - id: shellcheck

  # Commitlint - Conventional commits
  - repo: https://github.com/alessandrojcm/commitlint-pre-commit-hook
    rev: v9.18.0
    hooks:
      - id: commitlint
        stages: [commit-msg]
```

---

## Git Hooks (shell scripts)

### pre-commit (Secret + Lint)

```bash
#!/bin/bash
set -euo pipefail

echo "=== Pre-commit Security Checks ==="

# 1. Check for secrets
echo "[1/4] Scanning for secrets..."
if command -v gitleaks &>/dev/null; then
  gitleaks protect --staged --verbose || {
    echo "ERROR: Secrets detected! Remove them before committing."
    exit 1
  }
fi

# 2. Check for large files
echo "[2/4] Checking file sizes..."
MAX_SIZE=500000 # 500KB
for file in $(git diff --cached --name-only); do
  if [ -f "$file" ]; then
    size=$(wc -c <"$file")
    if [ "$size" -gt "$MAX_SIZE" ]; then
      echo "ERROR: $file is ${size} bytes (max ${MAX_SIZE})"
      exit 1
    fi
  fi
done

# 3. Check for TODO/FIXME/HACK in staged code
echo "[3/4] Checking for TODO/FIXME markers..."
MARKERS=$(git diff --cached --diff-filter=A -U0 | grep -E '^\+.*\b(TODO|FIXME|HACK|XXX)\b' || true)
if [ -n "$MARKERS" ]; then
  echo "WARNING: New TODO/FIXME markers found:"
  echo "$MARKERS"
  # Warning only, don't block
fi

# 4. Language-specific checks
echo "[4/4] Running language-specific checks..."
STAGED_FILES=$(git diff --cached --name-only)

# TypeScript/JavaScript
if echo "$STAGED_FILES" | grep -qE '\.(ts|tsx|js|jsx)$'; then
  if [ -f "package.json" ]; then
    npx eslint $(echo "$STAGED_FILES" | grep -E '\.(ts|tsx|js|jsx)$' | tr '\n' ' ') 2>/dev/null || {
      echo "ERROR: ESLint violations found"
      exit 1
    }
  fi
fi

# Python
if echo "$STAGED_FILES" | grep -qE '\.py$'; then
  if command -v ruff &>/dev/null; then
    ruff check $(echo "$STAGED_FILES" | grep -E '\.py$' | tr '\n' ' ') || {
      echo "ERROR: Ruff violations found"
      exit 1
    }
  fi
fi

# Go
if echo "$STAGED_FILES" | grep -qE '\.go$'; then
  if command -v golangci-lint &>/dev/null; then
    golangci-lint run --new-from-rev=HEAD 2>/dev/null || {
      echo "ERROR: Go lint violations found"
      exit 1
    }
  fi
fi

echo "=== All pre-commit checks passed ==="
```

### pre-push (Full Verification)

```bash
#!/bin/bash
set -euo pipefail

echo "=== Pre-push Verification ==="

# 1. Run tests
echo "[1/3] Running tests..."
if [ -f "package.json" ]; then
  npm test || { echo "ERROR: Tests failed"; exit 1; }
elif [ -f "pyproject.toml" ] || [ -f "setup.py" ]; then
  python -m pytest || { echo "ERROR: Tests failed"; exit 1; }
elif [ -f "go.mod" ]; then
  go test ./... || { echo "ERROR: Tests failed"; exit 1; }
fi

# 2. Build check
echo "[2/3] Verifying build..."
if [ -f "package.json" ]; then
  npm run build 2>/dev/null || { echo "ERROR: Build failed"; exit 1; }
fi

# 3. Security scan
echo "[3/3] Security scan..."
if command -v trivy &>/dev/null; then
  trivy fs --severity HIGH,CRITICAL --exit-code 1 . 2>/dev/null || {
    echo "WARNING: Security vulnerabilities detected"
  }
fi

echo "=== Pre-push verification passed ==="
```

### commit-msg (Conventional Commits)

```bash
#!/bin/bash
MSG=$(cat "$1")
PATTERN="^(feat|fix|docs|style|refactor|perf|test|chore|ci|build|revert)(\(.+\))?: .{1,72}$"

if ! echo "$MSG" | head -1 | grep -qE "$PATTERN"; then
  echo "ERROR: Commit message doesn't follow conventional commits format."
  echo "Expected: <type>(<scope>): <description>"
  echo "Types: feat, fix, docs, style, refactor, perf, test, chore, ci, build, revert"
  echo "Your message: $MSG"
  exit 1
fi

# Check message length
FIRST_LINE=$(echo "$MSG" | head -1)
if [ ${#FIRST_LINE} -gt 72 ]; then
  echo "ERROR: First line of commit message exceeds 72 characters (${#FIRST_LINE})"
  exit 1
fi
```

---

## Installation

### Pre-commit framework
```bash
pip install pre-commit
pre-commit install
pre-commit install --hook-type commit-msg
pre-commit run --all-files  # Test all hooks
```

### Manual git hooks
```bash
cp hooks/pre-commit .git/hooks/pre-commit
cp hooks/pre-push .git/hooks/pre-push
cp hooks/commit-msg .git/hooks/commit-msg
chmod +x .git/hooks/*
```
