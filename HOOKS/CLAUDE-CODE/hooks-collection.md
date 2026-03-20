# Claude Code Hooks Collection

> Pre-built hooks for security, quality, and workflow automation.

## Hook Types

| Type | Trigger | Use Case |
|------|---------|----------|
| `PreToolUse` | Before tool execution | Validation, parameter checks |
| `PostToolUse` | After tool execution | Auto-format, audit logging |
| `Notification` | On events | Alerts, notifications |
| `Stop` | Session ends | Final verification |

---

## Security Hooks

### 1. Secret Detection Hook (PreToolUse)

Prevents committing files containing secrets.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"$TOOL_INPUT\" | grep -iE '(api[_-]?key|secret|password|token|private[_-]?key|AWS_ACCESS|OPENAI_API)\\s*[:=]\\s*[\"'\\'][^\"'\\' ]{8,}' && echo 'BLOCKED: Potential secret detected in file content' && exit 1 || exit 0"
          }
        ]
      }
    ]
  }
}
```

### 2. Dangerous Command Blocker (PreToolUse)

Blocks destructive shell commands.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"$TOOL_INPUT\" | grep -E '(rm -rf /|:(){ :|:& };:|> /dev/sda|mkfs\\.|dd if=|chmod -R 777|curl.*\\| ?sh|wget.*\\| ?sh)' && echo 'BLOCKED: Dangerous command detected' && exit 1 || exit 0"
          }
        ]
      }
    ]
  }
}
```

### 3. SQL Injection Prevention (PreToolUse)

Detects potential SQL injection in code being written.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"$TOOL_INPUT\" | grep -nE '(\\$\\{.*\\}|\\+ *[a-zA-Z_]+|f\".*\\{.*\\}\"|`.*\\$)' | grep -iE '(SELECT|INSERT|UPDATE|DELETE|DROP|ALTER|EXEC|UNION)' && echo 'WARNING: Potential SQL injection - use parameterized queries' && exit 1 || exit 0"
          }
        ]
      }
    ]
  }
}
```

---

## Quality Hooks

### 4. Auto-Format on Save (PostToolUse)

Auto-formats files after writing.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "FILE=$(echo \"$TOOL_INPUT\" | jq -r '.file_path // .filePath // empty'); if [ -n \"$FILE\" ]; then case \"$FILE\" in *.ts|*.tsx|*.js|*.jsx) npx prettier --write \"$FILE\" 2>/dev/null ;; *.py) python3 -m black \"$FILE\" 2>/dev/null ;; *.go) gofmt -w \"$FILE\" 2>/dev/null ;; *.rs) rustfmt \"$FILE\" 2>/dev/null ;; esac; fi"
          }
        ]
      }
    ]
  }
}
```

### 5. File Size Guard (PreToolUse)

Prevents creating or editing files that are too large.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "CONTENT=$(echo \"$TOOL_INPUT\" | jq -r '.content // empty'); LINES=$(echo \"$CONTENT\" | wc -l); if [ \"$LINES\" -gt 800 ]; then echo \"BLOCKED: File exceeds 800 lines ($LINES lines). Split into smaller files.\" && exit 1; fi; exit 0"
          }
        ]
      }
    ]
  }
}
```

### 6. Test Requirement Check (PreToolUse)

Ensures test files exist before allowing commits.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "CMD=$(echo \"$TOOL_INPUT\" | jq -r '.command // empty'); if echo \"$CMD\" | grep -q 'git commit'; then CHANGED=$(git diff --cached --name-only | grep -E '\\.(ts|js|py|go)$' | grep -v '\\.test\\.' | grep -v '__test__' | grep -v '_test\\.'); for f in $CHANGED; do DIR=$(dirname \"$f\"); BASE=$(basename \"$f\" | sed 's/\\.[^.]*$//'); if ! find \"$DIR\" -name \"*${BASE}*test*\" -o -name \"*${BASE}*spec*\" | grep -q .; then echo \"WARNING: No test file found for $f\"; fi; done; fi; exit 0"
          }
        ]
      }
    ]
  }
}
```

---

## Workflow Hooks

### 7. Git Branch Protection (PreToolUse)

Prevents direct commits to main/master.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "CMD=$(echo \"$TOOL_INPUT\" | jq -r '.command // empty'); if echo \"$CMD\" | grep -qE 'git (commit|push)'; then BRANCH=$(git branch --show-current 2>/dev/null); if [ \"$BRANCH\" = 'main' ] || [ \"$BRANCH\" = 'master' ]; then echo 'BLOCKED: Cannot commit/push directly to main/master. Create a feature branch.' && exit 1; fi; fi; exit 0"
          }
        ]
      }
    ]
  }
}
```

### 8. Dependency Audit on Install (PostToolUse)

Runs security audit after installing packages.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "CMD=$(echo \"$TOOL_INPUT\" | jq -r '.command // empty'); if echo \"$CMD\" | grep -qE '(npm install|pnpm add|yarn add|pip install|go get)'; then echo '--- Running dependency security audit ---'; if [ -f 'package.json' ]; then npx audit-ci --moderate 2>/dev/null || echo 'WARN: Vulnerability found in dependencies'; elif [ -f 'requirements.txt' ]; then pip-audit 2>/dev/null || echo 'WARN: Vulnerability found in Python dependencies'; elif [ -f 'go.mod' ]; then govulncheck ./... 2>/dev/null || echo 'WARN: Vulnerability found in Go dependencies'; fi; fi; exit 0"
          }
        ]
      }
    ]
  }
}
```

### 9. Changelog Auto-Update (PostToolUse)

Adds commit messages to CHANGELOG on commit.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "CMD=$(echo \"$TOOL_INPUT\" | jq -r '.command // empty'); if echo \"$CMD\" | grep -q 'git commit'; then LAST_MSG=$(git log -1 --pretty=%s 2>/dev/null); DATE=$(date +%Y-%m-%d); if [ -f 'CHANGELOG.md' ]; then sed -i '' \"s/^## Unreleased/## Unreleased\\n- ${DATE}: ${LAST_MSG}/\" CHANGELOG.md 2>/dev/null; fi; fi; exit 0"
          }
        ]
      }
    ]
  }
}
```

### 10. Build Verification on Push (PreToolUse)

Runs build checks before allowing push.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "CMD=$(echo \"$TOOL_INPUT\" | jq -r '.command // empty'); if echo \"$CMD\" | grep -q 'git push'; then echo '--- Pre-push verification ---'; if [ -f 'package.json' ]; then npm run build 2>/dev/null || { echo 'BLOCKED: Build failed. Fix errors before pushing.' && exit 1; }; npm test 2>/dev/null || { echo 'BLOCKED: Tests failing. Fix before pushing.' && exit 1; }; fi; fi; exit 0"
          }
        ]
      }
    ]
  }
}
```

---

## Complete Hook Configuration

To use all hooks, add to your `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      { "matcher": "Write|Edit", "hooks": [{ "type": "command", "command": "..." }] },
      { "matcher": "Bash", "hooks": [{ "type": "command", "command": "..." }] }
    ],
    "PostToolUse": [
      { "matcher": "Write|Edit", "hooks": [{ "type": "command", "command": "..." }] },
      { "matcher": "Bash", "hooks": [{ "type": "command", "command": "..." }] }
    ]
  }
}
```

## Installation

1. Copy desired hooks to your `.claude/settings.json`
2. Replace `"..."` with the actual command strings from above
3. Test with a safe operation to verify hooks work
4. Combine multiple hooks for the same matcher using arrays
