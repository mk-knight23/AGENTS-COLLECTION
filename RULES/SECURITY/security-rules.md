# Security Rules & Hardening Guide

---

## OWASP Top 10 Prevention Rules

### 1. Injection (A03:2021)

```
RULE: Never concatenate user input into queries
FIX:  Parameterized queries / prepared statements / ORM

# SQL
BAD:  db.query(`SELECT * FROM users WHERE id = ${userId}`)
GOOD: db.query('SELECT * FROM users WHERE id = $1', [userId])

# NoSQL
BAD:  db.find({ user: req.body.user })
GOOD: db.find({ user: String(req.body.user) })

# Command
BAD:  exec(`convert ${filename}`)
GOOD: execFile('convert', [filename])
```

### 2. Broken Authentication (A07:2021)

```
RULE: Multi-layer authentication with rate limiting

□ Password hashing: bcrypt (cost 12+) or Argon2id
□ JWT: RS256/ES256, short expiration (15min access, 7d refresh)
□ Rate limiting: 5 failed attempts → 15 min lockout
□ MFA: TOTP or WebAuthn for sensitive accounts
□ Session: HttpOnly, Secure, SameSite=Lax cookies
□ Password requirements: Min 8 chars, check against breached lists
□ No credentials in URLs, logs, or error messages
```

### 3. Sensitive Data Exposure (A02:2021)

```
RULE: Encrypt everything, minimize data retention

□ TLS 1.3 for all connections (minimum TLS 1.2)
□ AES-256-GCM for data at rest
□ HSTS header with preload
□ No PII in logs, URLs, or error messages
□ Data classification: Public, Internal, Confidential, Restricted
□ Retention policy: Delete data when no longer needed
□ Field-level encryption for PII in databases
```

### 4. XXE (A05:2021 - Security Misconfiguration)

```
RULE: Disable external entity processing in all XML parsers

# Python
from defusedxml import ElementTree  # Not xml.etree.ElementTree

# Java
factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);

# Node.js
# Use libraries that disable DTD processing by default
```

### 5. Access Control (A01:2021)

```
RULE: Deny by default, verify on every request

□ RBAC or ABAC consistently applied
□ Verify object ownership (not just authentication)
□ No direct file/object ID references without auth check
□ Admin functions require additional verification
□ API endpoints respect same access rules as UI
□ CORS: specific allowed origins, never *
□ Rate limit: per-user, per-IP, per-endpoint
```

---

## Authentication Patterns

### JWT Best Practices
```javascript
// Token creation
const accessToken = jwt.sign(
  { sub: user.id, role: user.role },
  privateKey,
  {
    algorithm: 'RS256',         // Asymmetric — verify without secret
    expiresIn: '15m',           // Short-lived
    issuer: 'myapp.com',
    audience: 'myapp.com/api',
    jwtid: crypto.randomUUID(), // Unique token ID for revocation
  }
);

// Token verification
const decoded = jwt.verify(token, publicKey, {
  algorithms: ['RS256'],        // Reject other algorithms
  issuer: 'myapp.com',
  audience: 'myapp.com/api',
  clockTolerance: 30,           // 30s clock skew tolerance
});
```

### OAuth 2.0 + PKCE Flow
```
1. Client generates code_verifier (43-128 chars, [A-Za-z0-9-._~])
2. Client computes code_challenge = BASE64URL(SHA256(code_verifier))
3. Redirect to authorization server with code_challenge
4. User authenticates and authorizes
5. Callback with authorization_code
6. Exchange code + code_verifier for tokens
7. Server verifies: SHA256(code_verifier) == code_challenge
```

---

## API Security Rules

### Rate Limiting Tiers
```yaml
rate_limits:
  global:
    requests: 1000
    window: 1m

  per_user:
    requests: 100
    window: 1m

  authentication:
    requests: 5
    window: 15m
    lockout: 30m

  password_reset:
    requests: 3
    window: 1h

  file_upload:
    requests: 10
    window: 1h
    max_size: 10MB
```

### Input Validation Schema
```typescript
import { z } from 'zod';

const CreateUserSchema = z.object({
  name: z.string()
    .min(1).max(100)
    .regex(/^[a-zA-Z\s'-]+$/),
  email: z.string()
    .email()
    .max(254)
    .transform(e => e.toLowerCase()),
  password: z.string()
    .min(8).max(128)
    .regex(/[A-Z]/, 'Must contain uppercase')
    .regex(/[a-z]/, 'Must contain lowercase')
    .regex(/[0-9]/, 'Must contain number'),
  age: z.number()
    .int()
    .min(13).max(150)
    .optional(),
}).strict(); // Reject unknown fields
```

---

## Container Security Checklist

```dockerfile
# Secure Dockerfile template
FROM node:20-slim AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

FROM gcr.io/distroless/nodejs20-debian12
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
USER nonroot:nonroot
EXPOSE 8080
CMD ["dist/index.js"]
```

### Checklist
```
□ Multi-stage build (separate build and runtime)
□ Minimal base image (distroless, Alpine, slim)
□ Non-root user (USER directive)
□ No secrets in image layers
□ Pinned base image versions (digest or semver)
□ Read-only filesystem where possible
□ No unnecessary packages installed
□ Health check defined
□ .dockerignore excludes .git, node_modules, .env
□ Image scanning in CI (Trivy, Snyk)
```

---

## Security Headers Quick Reference

| Header | Value | Why |
|--------|-------|-----|
| `Strict-Transport-Security` | `max-age=63072000; includeSubDomains; preload` | Force HTTPS |
| `Content-Security-Policy` | `default-src 'none'; script-src 'self'...` | Prevent XSS |
| `X-Content-Type-Options` | `nosniff` | Prevent MIME sniffing |
| `X-Frame-Options` | `DENY` | Prevent clickjacking |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | Limit referrer leak |
| `Permissions-Policy` | `camera=(), microphone=()...` | Restrict browser APIs |
| `Cross-Origin-Opener-Policy` | `same-origin` | Process isolation |

---

## Secret Management Rules

```
1. NEVER in code: API keys, passwords, tokens, certificates
2. ALWAYS use: Environment variables, secret managers (Vault, AWS SM)
3. ROTATE on schedule: 90 days for keys, immediately if exposed
4. AUDIT access: Log all secret access with identity
5. ENCRYPT at rest: AES-256-GCM for stored secrets
6. SCOPE minimally: Per-service, per-environment secrets
7. DETECT in CI: Gitleaks, TruffleHog in pre-commit + CI
```

### `.env.example` Template
```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/mydb_dev

# Authentication
JWT_PRIVATE_KEY_PATH=./keys/private.pem
JWT_PUBLIC_KEY_PATH=./keys/public.pem
JWT_EXPIRATION=15m

# External APIs
STRIPE_SECRET_KEY=sk_test_...
SENDGRID_API_KEY=SG.test...

# Application
NODE_ENV=development
PORT=3000
LOG_LEVEL=debug
CORS_ORIGINS=http://localhost:3000
```
