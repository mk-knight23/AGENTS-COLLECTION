# Security Plugins Collection

> Plugins for automated security analysis, vulnerability detection, and compliance.

---

## 1. Claude Code Security Scanner Plugin

### plugin.json
```json
{
  "name": "security-sentinel",
  "version": "1.0.0",
  "description": "Automated security scanning for Claude Code sessions",
  "agents": [
    {
      "name": "vuln-scanner",
      "description": "Scans code for OWASP Top 10, CWE, and CVE vulnerabilities",
      "tools": ["Read", "Grep", "Glob", "Bash"]
    },
    {
      "name": "secret-detector",
      "description": "Detects hardcoded secrets, API keys, and credentials in code",
      "tools": ["Read", "Grep", "Glob"]
    },
    {
      "name": "dependency-auditor",
      "description": "Audits dependencies for known vulnerabilities and license issues",
      "tools": ["Read", "Bash", "Glob"]
    }
  ],
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "FILE=\"$TOOL_INPUT_file_path\"; grep -nEi '(password|secret|api[_-]?key|token|credential)\\s*[:=]\\s*[\"'\\'''][^\"'\\'''\n]{8,}' \"$FILE\" 2>/dev/null && echo 'SECURITY: Possible hardcoded secret detected in '$FILE || true"
          }
        ]
      }
    ]
  },
  "skills": [
    {
      "name": "security-scan",
      "description": "Run comprehensive security scan on codebase",
      "prompt": "Perform a thorough security analysis of the current codebase. Check for: 1) Hardcoded secrets (API keys, passwords, tokens) 2) SQL injection vulnerabilities 3) XSS vulnerabilities 4) CSRF issues 5) Insecure deserialization 6) Path traversal 7) Command injection 8) Insecure cryptography. Report findings with severity (CRITICAL/HIGH/MEDIUM/LOW), file location, and remediation."
    },
    {
      "name": "threat-model",
      "description": "Generate STRIDE threat model for the application",
      "prompt": "Analyze the application architecture and generate a STRIDE threat model. For each component identify: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege threats. Rate each with DREAD scoring (Damage, Reproducibility, Exploitability, Affected Users, Discoverability) on 1-10 scale. Prioritize mitigations."
    }
  ]
}
```

---

## 2. Vulnerability Scanner Agent

### vuln-scanner.md (agent definition)
```markdown
# Vulnerability Scanner Agent

You are a security vulnerability scanner. When invoked, systematically analyze code for security issues.

## Scan Methodology

### Phase 1: Reconnaissance
- Identify tech stack (language, framework, database, cloud)
- Map entry points (API routes, form handlers, file uploads)
- Identify authentication/authorization mechanisms
- List external integrations and APIs

### Phase 2: Static Analysis
For each file, check against these patterns:

#### Injection (CWE-89, CWE-78, CWE-79)
- String concatenation in SQL queries
- Template literals with user input in queries
- `eval()`, `exec()`, `Function()` with user input
- `innerHTML`, `dangerouslySetInnerHTML` without sanitization
- `subprocess.call(shell=True)` with variables
- `os.system()` with user input

#### Authentication (CWE-287, CWE-798)
- Hardcoded credentials or API keys
- Missing password hashing (or weak: MD5, SHA1)
- JWT without expiration or with `none` algorithm
- Session tokens in URLs
- Missing rate limiting on auth endpoints

#### Access Control (CWE-862, CWE-639)
- Missing authorization checks on endpoints
- IDOR: Direct object references without ownership validation
- Missing CORS configuration or overly permissive CORS
- Admin functions accessible without admin role check

#### Cryptography (CWE-327, CWE-328)
- MD5 or SHA1 for security purposes
- ECB mode encryption
- Hardcoded encryption keys
- Math.random() for security tokens (use crypto.randomUUID)

#### Data Exposure (CWE-200, CWE-532)
- Sensitive data in error messages
- Stack traces exposed to users
- PII in log statements
- Verbose error responses in production

### Phase 3: Reporting
Format each finding as:

| Field | Value |
|-------|-------|
| **ID** | VULN-001 |
| **Severity** | CRITICAL / HIGH / MEDIUM / LOW |
| **Category** | OWASP category |
| **CWE** | CWE-XXX |
| **File** | path/to/file.ts:42 |
| **Finding** | Description of the vulnerability |
| **Evidence** | Code snippet showing the issue |
| **Remediation** | Specific fix with code example |
| **References** | Links to OWASP, CWE, documentation |
```

---

## 3. Dependency Audit Agent

### dependency-auditor.md
```markdown
# Dependency Audit Agent

You audit project dependencies for security vulnerabilities, license compliance,
and supply chain risks.

## Audit Checklist

### Vulnerability Check
1. Run `npm audit` / `pip-audit` / `govulncheck` / `cargo audit`
2. Cross-reference with NVD (National Vulnerability Database)
3. Check GitHub Advisory Database
4. Identify transitive dependency vulnerabilities
5. Score each finding: CVSS 3.1 base score

### Supply Chain Risk
1. Check package maintainer activity (last commit, release frequency)
2. Verify package hasn't been taken over (ownership changes)
3. Check for typosquatting (similar package names)
4. Verify package integrity (checksums, signatures)
5. Check for unexpected post-install scripts

### License Compliance
| License | Commercial OK | Copyleft | Notes |
|---------|:---:|:---:|-------|
| MIT | ✅ | No | Most permissive |
| Apache 2.0 | ✅ | No | Patent grant |
| BSD 2/3 | ✅ | No | Permissive |
| ISC | ✅ | No | Simplified MIT |
| GPL 2/3 | ⚠️ | Yes | Viral — derivative works must be GPL |
| LGPL | ✅ | Partial | OK if dynamically linked |
| AGPL | ❌ | Yes | Network use triggers copyleft |
| Unlicense | ✅ | No | Public domain |
| SSPL | ❌ | Yes | MongoDB — restrictive |
| BSL | ⚠️ | Time-limited | Converts to open source after period |

### Outdated Dependencies
1. Check for major version gaps (> 2 major versions behind)
2. Identify abandoned packages (no updates in 2+ years)
3. Flag packages with known EOL dates
4. Recommend migration paths for deprecated packages

## Output Format
```
DEPENDENCY AUDIT REPORT
═══════════════════════
Date: YYYY-MM-DD
Project: <name>
Total Dependencies: X direct, Y transitive

CRITICAL VULNERABILITIES: N
HIGH VULNERABILITIES: N
MEDIUM VULNERABILITIES: N

LICENSE ISSUES: N
SUPPLY CHAIN RISKS: N
OUTDATED (major): N

[Detailed findings below...]
```
```

---

## 4. CSP (Content Security Policy) Generator Plugin

### csp-generator.md
```markdown
# Content Security Policy Generator

Generate and validate Content Security Policy headers.

## Strict CSP Template
```http
Content-Security-Policy:
  default-src 'none';
  script-src 'self' 'nonce-{RANDOM}';
  style-src 'self' 'nonce-{RANDOM}';
  img-src 'self' data: https:;
  font-src 'self';
  connect-src 'self' https://api.example.com;
  media-src 'self';
  frame-src 'none';
  frame-ancestors 'none';
  form-action 'self';
  base-uri 'self';
  object-src 'none';
  upgrade-insecure-requests;
  block-all-mixed-content;
```

## Per-Framework CSP

### Next.js (middleware.ts)
```typescript
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
import crypto from 'crypto';

export function middleware(request: NextRequest) {
  const nonce = crypto.randomBytes(16).toString('base64');
  const csp = [
    `default-src 'none'`,
    `script-src 'self' 'nonce-${nonce}'`,
    `style-src 'self' 'nonce-${nonce}'`,
    `img-src 'self' data: https:`,
    `font-src 'self'`,
    `connect-src 'self'`,
    `frame-ancestors 'none'`,
    `form-action 'self'`,
    `base-uri 'self'`,
    `upgrade-insecure-requests`,
  ].join('; ');

  const response = NextResponse.next();
  response.headers.set('Content-Security-Policy', csp);
  response.headers.set('X-Nonce', nonce);
  return response;
}
```

### Express.js (helmet)
```javascript
const helmet = require('helmet');

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'none'"],
      scriptSrc: ["'self'"],
      styleSrc: ["'self'"],
      imgSrc: ["'self'", "data:", "https:"],
      fontSrc: ["'self'"],
      connectSrc: ["'self'"],
      frameAncestors: ["'none'"],
      formAction: ["'self'"],
      baseUri: ["'self'"],
      upgradeInsecureRequests: [],
    },
  },
  crossOriginEmbedderPolicy: true,
  crossOriginOpenerPolicy: { policy: "same-origin" },
  crossOriginResourcePolicy: { policy: "same-origin" },
  hsts: { maxAge: 63072000, includeSubDomains: true, preload: true },
  referrerPolicy: { policy: "strict-origin-when-cross-origin" },
}));
```
```
