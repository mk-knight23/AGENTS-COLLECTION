# Quality Hooks Collection

> Pre-commit and CI hooks for code quality, formatting, linting, and test enforcement.

---

## Universal Quality Hook (.pre-commit-config.yaml)

```yaml
repos:
  # General file quality
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
        args: [--allow-multiple-documents]
      - id: check-json
      - id: check-toml
      - id: check-xml
      - id: check-merge-conflict
      - id: check-case-conflict
      - id: check-symlinks
      - id: check-added-large-files
        args: [--maxkb=500]
      - id: mixed-line-ending
        args: [--fix=lf]
      - id: fix-byte-order-marker
      - id: check-executables-have-shebangs
      - id: check-shebang-scripts-are-executable
      - id: debug-statements        # Python: no pdb/breakpoint
      - id: name-tests-test         # Python: test files start with test_
        args: [--pytest-test-first]

  # Markdown
  - repo: https://github.com/igorshubovych/markdownlint-cli
    rev: v0.42.0
    hooks:
      - id: markdownlint
        args: [--fix]

  # Spell check
  - repo: https://github.com/codespell-project/codespell
    rev: v2.3.0
    hooks:
      - id: codespell
        args: [-L, "ths,te,nd"]  # Ignore false positives

  # Prettier (JS/TS/CSS/HTML/JSON/YAML/MD)
  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v4.0.0-alpha.8
    hooks:
      - id: prettier
        types_or: [javascript, jsx, ts, tsx, css, scss, json, yaml, markdown, html]

  # ESLint (JS/TS)
  - repo: https://github.com/pre-commit/mirrors-eslint
    rev: v9.14.0
    hooks:
      - id: eslint
        files: \.[jt]sx?$
        types: [file]
        additional_dependencies:
          - eslint@9.14.0
          - typescript-eslint@8.13.0

  # Ruff (Python linting + formatting)
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.7.4
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
      - id: ruff-format

  # mypy (Python type checking)
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.13.0
    hooks:
      - id: mypy
        additional_dependencies: [types-requests, types-pyyaml]

  # Go
  - repo: https://github.com/golangci/golangci-lint
    rev: v1.62.0
    hooks:
      - id: golangci-lint

  - repo: https://github.com/dnephin/pre-commit-golang
    rev: v0.5.1
    hooks:
      - id: go-fmt
      - id: go-vet
      - id: go-imports

  # Rust
  - repo: https://github.com/doublify/pre-commit-rust
    rev: v1.0
    hooks:
      - id: fmt
      - id: clippy
        args: [--all-targets, --all-features, --, -D, warnings]

  # Terraform
  - repo: https://github.com/antonbabenko/pre-commit-terraform
    rev: v1.96.1
    hooks:
      - id: terraform_fmt
      - id: terraform_validate
      - id: terraform_tflint
      - id: terraform_docs

  # Docker
  - repo: https://github.com/hadolint/hadolint
    rev: v2.12.0
    hooks:
      - id: hadolint

  # YAML linting
  - repo: https://github.com/adrienverge/yamllint
    rev: v1.35.1
    hooks:
      - id: yamllint
        args: [-d, "{extends: relaxed, rules: {line-length: {max: 120}}}"]

  # Conventional commits
  - repo: https://github.com/compilerla/conventional-pre-commit
    rev: v3.6.0
    hooks:
      - id: conventional-pre-commit
        stages: [commit-msg]
        args: [feat, fix, docs, style, refactor, perf, test, chore, ci, build, revert]
```

---

## Claude Code Quality Hooks (settings.json)

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Quality check: Verify immutability, error handling, file size < 800 lines'"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "FILE=\"$TOOL_INPUT_file_path\"; if [ -f \"$FILE\" ]; then LINES=$(wc -l < \"$FILE\"); if [ \"$LINES\" -gt 800 ]; then echo \"WARNING: File exceeds 800 lines ($LINES). Consider splitting.\"; fi; fi"
          }
        ]
      },
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "FILE=\"$TOOL_INPUT_file_path\"; EXT=\"${FILE##*.}\"; case \"$EXT\" in ts|tsx|js|jsx) npx prettier --check \"$FILE\" 2>/dev/null || echo 'Format warning: Run prettier' ;; py) ruff check \"$FILE\" 2>/dev/null || echo 'Lint warning: Run ruff' ;; esac"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo '=== Session Quality Summary ===' && echo 'Remember: Run tests before committing'"
          }
        ]
      }
    ]
  }
}
```

---

## Language-Specific Lint Configs

### TypeScript — eslint.config.mjs
```javascript
import tseslint from 'typescript-eslint';
import eslint from '@eslint/js';

export default tseslint.config(
  eslint.configs.recommended,
  ...tseslint.configs.strictTypeChecked,
  {
    rules: {
      '@typescript-eslint/no-explicit-any': 'error',
      '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
      '@typescript-eslint/strict-boolean-expressions': 'error',
      '@typescript-eslint/no-floating-promises': 'error',
      '@typescript-eslint/no-misused-promises': 'error',
      '@typescript-eslint/prefer-readonly': 'error',
      'no-console': ['warn', { allow: ['warn', 'error'] }],
      'no-debugger': 'error',
      'prefer-const': 'error',
      'no-var': 'error',
      eqeqeq: ['error', 'always'],
      'no-eval': 'error',
      'no-implied-eval': 'error',
    },
  }
);
```

### Python — pyproject.toml (ruff)
```toml
[tool.ruff]
target-version = "py312"
line-length = 100
fix = true

[tool.ruff.lint]
select = [
  "E",   # pycodestyle errors
  "W",   # pycodestyle warnings
  "F",   # pyflakes
  "I",   # isort
  "N",   # pep8-naming
  "UP",  # pyupgrade
  "B",   # flake8-bugbear
  "S",   # flake8-bandit (security)
  "A",   # flake8-builtins
  "C4",  # flake8-comprehensions
  "DTZ", # flake8-datetimez
  "T20", # flake8-print
  "SIM", # flake8-simplify
  "TCH", # flake8-type-checking
  "RUF", # ruff-specific
]
ignore = ["E501"]  # line length handled by formatter

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = ["S101"]  # Allow assert in tests

[tool.mypy]
python_version = "3.12"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

### Go — .golangci.yml
```yaml
linters:
  enable:
    - errcheck       # Unchecked errors
    - govet          # Suspicious constructs
    - staticcheck    # Advanced analysis
    - gosimple       # Simplify code
    - ineffassign    # Unused assignments
    - unused         # Unused code
    - revive         # Extensible linter
    - gocritic       # Opinionated checks
    - gosec          # Security issues
    - bodyclose      # HTTP body close
    - contextcheck   # Context propagation
    - nilerr         # nil error returns
    - exhaustive     # Exhaustive switch
    - prealloc       # Slice preallocation

linters-settings:
  revive:
    rules:
      - name: exported
        arguments: [checkPrivateReceivers]
      - name: blank-imports
      - name: context-as-argument
      - name: error-return
      - name: error-naming
      - name: if-return
      - name: increment-decrement
      - name: var-naming
      - name: range
      - name: receiver-naming
      - name: time-naming
      - name: unexported-return
      - name: errorf
      - name: empty-block
      - name: superfluous-else
      - name: unreachable-code
  gosec:
    severity: medium
    confidence: medium

issues:
  max-issues-per-linter: 50
  max-same-issues: 5

run:
  timeout: 5m
  tests: true
```

---

## Test Gate Hook (pre-push)

```bash
#!/bin/bash
set -euo pipefail

echo "=== Pre-Push Quality Gate ==="

# Detect project type and run appropriate tests
if [ -f "package.json" ]; then
  echo "[1/3] TypeScript/JavaScript tests..."
  npm run type-check 2>/dev/null || npx tsc --noEmit || true
  npm test -- --passWithNoTests || { echo "FAIL: Tests failed"; exit 1; }

  echo "[2/3] Lint check..."
  npm run lint 2>/dev/null || npx eslint . --ext .ts,.tsx || true

  echo "[3/3] Build verification..."
  npm run build 2>/dev/null || { echo "FAIL: Build failed"; exit 1; }

elif [ -f "pyproject.toml" ] || [ -f "setup.py" ]; then
  echo "[1/3] Python tests..."
  python -m pytest --tb=short -q || { echo "FAIL: Tests failed"; exit 1; }

  echo "[2/3] Type check..."
  mypy . 2>/dev/null || true

  echo "[3/3] Lint..."
  ruff check . 2>/dev/null || true

elif [ -f "go.mod" ]; then
  echo "[1/3] Go tests..."
  go test ./... -count=1 || { echo "FAIL: Tests failed"; exit 1; }

  echo "[2/3] Go vet..."
  go vet ./... || { echo "FAIL: go vet failed"; exit 1; }

  echo "[3/3] Build..."
  go build ./... || { echo "FAIL: Build failed"; exit 1; }
fi

echo "=== Quality gate passed ==="
```
