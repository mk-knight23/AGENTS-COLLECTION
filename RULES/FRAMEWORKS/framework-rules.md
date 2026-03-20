# Framework-Specific Rules Collection

---

## React / Next.js Rules

### Rules

1. **Server Components first** — Default to RSC, add `'use client'` only when needed
2. **No prop drilling** — Use Context, Zustand, or composition patterns
3. **Colocation** — Components, styles, tests in same directory
4. **Custom hooks for logic** — Extract reusable logic into `use*` hooks
5. **Suspense boundaries** — Wrap async components with `<Suspense>`
6. **Error boundaries** — Wrap sections prone to failure
7. **Memoization with purpose** — Only `useMemo`/`useCallback` when measured
8. **No index keys for dynamic lists** — Use stable unique IDs
9. **Controlled forms** — Use React Hook Form or conform
10. **Image optimization** — Always use `next/image` or equivalent

### Next.js App Router Patterns
```
app/
├── (auth)/           # Route group (no URL impact)
│   ├── login/page.tsx
│   └── register/page.tsx
├── (dashboard)/
│   ├── layout.tsx    # Shared dashboard layout
│   ├── page.tsx      # Dashboard home
│   └── settings/page.tsx
├── api/              # Route Handlers
│   └── users/route.ts
├── error.tsx         # Error boundary
├── loading.tsx       # Loading UI
├── not-found.tsx     # 404 page
└── layout.tsx        # Root layout
```

### Component Pattern
```tsx
// Feature component with proper patterns
interface Props {
  readonly userId: string;
}

export function UserProfile({ userId }: Props) {
  // Server component by default
  // No 'use client' needed for data fetching
  return (
    <Suspense fallback={<UserProfileSkeleton />}>
      <UserProfileContent userId={userId} />
    </Suspense>
  );
}
```

---

## Express / Fastify Rules

### Rules

1. **Middleware ordering** — Security headers → CORS → Auth → Routes → Error handler
2. **Input validation** — Zod/Joi on every endpoint, validate before processing
3. **Error handling middleware** — Central error handler, never expose stack traces
4. **Rate limiting** — Per-endpoint rate limits, stricter for auth endpoints
5. **Request logging** — Structured logging with correlation IDs
6. **Graceful shutdown** — Handle SIGTERM, drain connections, close DB pools
7. **No business logic in routes** — Controllers call services, services call repositories
8. **Response envelope** — `{ success: boolean, data?: T, error?: string }`
9. **Pagination** — Cursor-based for large datasets, offset for small
10. **Health checks** — `/health` (liveness), `/ready` (readiness with DB check)

### Express Security Middleware Stack
```javascript
// middleware/security.js
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';
import cors from 'cors';
import hpp from 'hpp';
import mongoSanitize from 'express-mongo-sanitize';

export function securityMiddleware(app) {
  app.use(helmet());
  app.use(cors({ origin: process.env.ALLOWED_ORIGINS?.split(','), credentials: true }));
  app.use(hpp());                    // HTTP parameter pollution
  app.use(mongoSanitize());         // NoSQL injection prevention
  app.use(rateLimit({
    windowMs: 15 * 60 * 1000,       // 15 minutes
    max: 100,                        // 100 requests per window
    standardHeaders: true,
    legacyHeaders: false,
  }));
  app.use(rateLimit({
    windowMs: 60 * 1000,             // 1 minute
    max: 5,                          // 5 login attempts
    skipSuccessfulRequests: true,
  }).bind(null, '/api/auth/login'));
}
```

---

## Django / FastAPI Rules

### Django Rules

1. **Fat models, thin views** — Business logic in models/managers
2. **Custom user model** — Always `AbstractUser` from the start
3. **Signals sparingly** — Prefer explicit method calls over signals
4. **Querysets, not loops** — `User.objects.filter()` not `for user in User.objects.all()`
5. **`select_related` / `prefetch_related`** — Avoid N+1 queries
6. **Migrations are code** — Review, test, and version control them
7. **Settings module** — `base.py`, `dev.py`, `prod.py`, `test.py`
8. **Django REST Framework** — Serializers for validation and response shaping
9. **Celery for async** — Background tasks, not in request/response cycle
10. **Factory Boy for tests** — Not fixtures, not raw model creation

### FastAPI Rules

1. **Pydantic models** — Request/response schemas with validation
2. **Dependency injection** — Use `Depends()` for shared logic
3. **Async handlers** — Use `async def` for I/O-bound endpoints
4. **SQLAlchemy async** — `AsyncSession` with proper connection pooling
5. **Middleware order** — CORS → Auth → Logging → Routes
6. **Background tasks** — `BackgroundTasks` for fire-and-forget
7. **API versioning** — `/api/v1/` prefix, router per version
8. **OpenAPI customization** — Tags, descriptions, examples in schemas
9. **Structured responses** — Generic response model with typing
10. **Health endpoint** — Include DB connectivity check

### FastAPI Pattern
```python
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, Field

class CreateUserRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: str = Field(pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')

class UserResponse(BaseModel):
    id: str
    name: str
    email: str

    model_config = {"from_attributes": True}

@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    body: CreateUserRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> UserResponse:
    user = await user_service.create(db, body)
    return UserResponse.model_validate(user)
```

---

## Spring Boot Rules

### Rules

1. **Constructor injection** — No `@Autowired` on fields
2. **Profiles** — `@Profile("dev")`, `@Profile("prod")` for environment-specific beans
3. **`@Transactional` on service layer** — Not on repositories or controllers
4. **DTOs for API** — Never expose entities directly
5. **Global exception handler** — `@ControllerAdvice` with `@ExceptionHandler`
6. **Actuator** — Enable health, info, metrics endpoints
7. **Testcontainers** — Real DB in integration tests
8. **MapStruct** — Compile-time DTO mapping, not manual
9. **Flyway/Liquibase** — Version-controlled migrations
10. **Jackson configuration** — Fail on unknown properties, use snake_case

### Spring Security Configuration
```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        return http
            .csrf(csrf -> csrf.csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse()))
            .cors(cors -> cors.configurationSource(corsConfig()))
            .sessionManagement(s -> s.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/public/**").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .anyRequest().authenticated()
            )
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(Customizer.withDefaults()))
            .build();
    }
}
```

---

## Terraform / IaC Rules

### Rules

1. **Modules for reuse** — 3+ occurrences = create a module
2. **Remote state** — S3/GCS backend with state locking (DynamoDB/GCS)
3. **Workspaces or directories** — Per-environment isolation
4. **`terraform fmt`** — Format before every commit
5. **`terraform validate`** — Run in CI before plan
6. **Plan before apply** — Always review `terraform plan` output
7. **Pin provider versions** — `required_providers { aws = { version = "~> 5.0" } }`
8. **No hardcoded values** — Variables with defaults, tfvars per environment
9. **Tags on everything** — `Environment`, `Team`, `CostCenter`, `ManagedBy`
10. **Least privilege IAM** — Specific permissions, never `*`

### Terraform Module Structure
```
modules/
└── vpc/
    ├── main.tf          # Resource definitions
    ├── variables.tf     # Input variables with descriptions
    ├── outputs.tf       # Output values
    ├── versions.tf      # Required providers + versions
    ├── data.tf          # Data sources
    └── locals.tf        # Local values
```

---

## Kubernetes Rules

### Rules

1. **Resource limits** — Always set CPU/memory requests AND limits
2. **Liveness + readiness probes** — Every container, distinct endpoints
3. **Pod Disruption Budgets** — `minAvailable` for critical services
4. **Network Policies** — Default deny, whitelist needed traffic
5. **Non-root containers** — `securityContext.runAsNonRoot: true`
6. **No `:latest` tag** — Pin to specific image digests or semver
7. **ConfigMaps for config, Secrets for secrets** — Never env vars for secrets
8. **HPA for scaling** — CPU + custom metrics (queue depth, request rate)
9. **Namespaces for isolation** — Per-team or per-environment
10. **RBAC** — Least privilege, service accounts per deployment

### Pod Security Standards
```yaml
apiVersion: v1
kind: Pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 1000
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: app
      image: myapp@sha256:abc123...
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: ["ALL"]
      resources:
        requests:
          cpu: 100m
          memory: 128Mi
        limits:
          cpu: 500m
          memory: 512Mi
      livenessProbe:
        httpGet:
          path: /health
          port: 8080
        initialDelaySeconds: 10
        periodSeconds: 10
      readinessProbe:
        httpGet:
          path: /ready
          port: 8080
        initialDelaySeconds: 5
        periodSeconds: 5
```
