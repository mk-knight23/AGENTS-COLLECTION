# Friday AI Teammate v1.0 - Industry-Grade Upgrade Plan

## Context

Friday AI Teammate is currently at v0.3.0 with a solid foundation. The exploration revealed:

**Already Implemented (Production-Ready):**
- Three-state circuit breaker (CLOSED/HALF_OPEN/OPEN) with proper transitions
- Rate limiting (100 calls/hour) with persistence and auto-reset
- 24-hour session persistence with full lifecycle management
- 16 tools with structured responses and good error handling
- Pydantic-based configuration system
- Safety features (approval policies, dangerous command detection)

**Critical Gaps for v1.0:**
- Minimal error hierarchy (only AgentError, ConfigError)
- No retry logic for network operations
- No structured audit logging
- No health check system
- No metrics/observability
- No connection pooling for databases
- Limited secret management (basic pattern scrubbing only)

---

## Implementation Plan

### Phase 1: Foundation - Error Hierarchy & Audit System (Week 1)

**1.1 Enhanced Error Hierarchy**
Create `/friday_ai/utils/error hierarchy.py` with industry-standard error taxonomy:

```python
class FridayError(Exception):
    """Base exception with error codes, retryable flag, and structured context."""
    code: str
    message: str
    details: dict
    retryable: bool
    trace_id: str

class ToolExecutionError(FridayError): ...
class ValidationError(FridayError): ...
class AuthenticationError(FridayError): ...
class AuthorizationError(FridayError): ...
class RateLimitError(FridayError): ...
class ResourceExhaustedError(FridayError): ...
class CircuitOpenError(FridayError): ...
class TimeoutError(FridayError): ...
class DependencyError(FridayError): ...
```

**Files to modify:**
- `friday_ai/utils/errors.py` - Refactor into comprehensive hierarchy (lines 1-50)

**1.2 Structured Audit Logging**
Create `/friday_ai/security/audit_logger.py`:

```python
class AuditLogger:
    """Tamper-evident audit logging with structured JSON format."""

    LOG_FORMAT = {
        "timestamp": "ISO8601",
        "event_type": "tool_execution|file_operation|auth_event|config_change",
        "user": "string",
        "action": "string",
        "resource": "string",
        "result": "success|failure",
        "details": "object",
        "trace_id": "string",
        "checksum": "sha256"  # Tamper detection
    }
```

**Files to create:**
- `friday_ai/security/__init__.py`
- `friday_ai/security/audit_logger.py`
- `friday_ai/security/secret_manager.py` - Enhanced secret handling with keyring integration

**1.3 Input Validation Layer**
Create `/friday_ai/security/validators.py`:

```python
class InputValidator:
    """Comprehensive input validation for security."""

    def validate_path(self, path: str, allow_absolute: bool = False) -> ValidatedPath
    def validate_command(self, cmd: str) -> ValidatedCommand
    def validate_sql(self, query: str) -> ValidatedSQL
    def validate_url(self, url: str) -> ValidatedURL
```

---

### Phase 2: Resilience - Retry, Health & Circuit Breaker (Week 2)

**2.1 Retry Policy with Exponential Backoff**
Create `/friday_ai/resilience/retry.py`:

```python
class RetryPolicy:
    """Configurable retry with exponential backoff and jitter."""

    max_retries: int = 3
    base_delay: float = 1.0
    max_delay: float = 60.0
    exponential_base: float = 2.0
    jitter: bool = True

    retryable_exceptions: List[Type[Exception]] = [
        ConnectionError,
        TimeoutError,
        RateLimitError,
    ]
```

**Files to create:**
- `friday_ai/resilience/__init__.py`
- `friday_ai/resilience/retry.py`
- `friday_ai/resilience/health_checks.py`

**2.2 Health Check System**
Create `/friday_ai/resilience/health_checks.py`:

```python
class HealthCheckSystem:
    """Kubernetes-style health checks."""

    async def liveness_check(self) -> HealthStatus  # /health
    async def readiness_check(self) -> HealthStatus  # /ready
    async def dependency_check(self, service: str) -> HealthStatus
```

**2.3 Enhanced Circuit Breaker Metrics**
Modify `friday_ai/agent/autonomous_loop.py` (lines 358-512):
- Add metrics collection to CircuitBreaker class
- Add event emission on state changes
- Add sliding window failure rate calculation

---

### Phase 3: Observability - Metrics & Tracing (Week 3)

**3.1 Metrics Collection**
Create `/friday_ai/observability/metrics.py`:

```python
class MetricsCollector:
    """Prometheus-compatible metrics collection."""

    def counter(self, name: str, value: int, tags: dict)
    def gauge(self, name: str, value: float, tags: dict)
    def histogram(self, name: str, value: float, tags: dict)
    def timing(self, name: str, duration_ms: float, tags: dict)

    def export_prometheus(self) -> str
    def export_json(self) -> dict
```

**Files to create:**
- `friday_ai/observability/__init__.py`
- `friday_ai/observability/metrics.py`
- `friday_ai/observability/tracing.py` - Distributed tracing support
- `friday_ai/observability/logging_config.py` - Structured JSON logging

**3.2 Tool Instrumentation**
Modify `friday_ai/tools/registry.py` (lines 1-200):
- Add metrics collection for tool execution latency
- Add error rate tracking per tool
- Add active operation gauges

---

### Phase 4: Security Hardening (Week 4)

**4.1 Secret Management Enhancement**
Modify and enhance secret handling:

```python
class SecretManager:
    """Industry-standard secret handling."""

    SECRET_PATTERNS = [
        r'(?i)(api[_-]?key|apikey)',
        r'(?i)(secret|password|passwd|pwd)',
        r'(?i)(token|bearer|auth)',
        r'(?i)(credential|private[_-]?key)',
    ]

    def redact(self, text: str) -> str
    def secure_store(self, key: str, value: str) -> None  # keyring integration
    def secure_retrieve(self, key: str) -> str
```

**Files to modify:**
- `friday_ai/utils/text.py` - Enhance scrub_secrets with regex patterns (lines 1-50)
- `friday_ai/config/config.py` - Add secret resolution for MCP servers (lines 23-51)

**4.2 Tool Security Enhancements**
Modify network tools to add retry logic:
- `friday_ai/tools/builtin/http_request.py` - Add retry decorator
- `friday_ai/tools/builtin/web_fetch.py` - Add retry decorator
- `friday_ai/tools/builtin/web_search.py` - Add rate limit protection

---

### Phase 5: Database Layer (Week 5)

**5.1 Connection Pool Management**
Create `/friday_ai/database/pool.py`:

```python
class DatabaseConnectionPool:
    """Production database connection pooling."""

    min_connections: int = 2
    max_connections: int = 10
    connection_timeout: float = 5.0
    query_timeout: float = 30.0

    SUPPORTED_BACKENDS = ['postgresql', 'mysql', 'sqlite']

    async def get_connection(self) -> Connection
    async def execute(self, query: str, params: tuple, timeout: float = None) -> Result
    async def transaction(self) -> AsyncContextManager[Transaction]
```

**Files to create:**
- `friday_ai/database/__init__.py`
- `friday_ai/database/pool.py`
- `friday_ai/database/migrations.py`

**5.2 Database Tool Enhancement**
Modify `friday_ai/tools/builtin/database.py` (lines 1-374):
- Add timeout handling for queries
- Add connection pooling
- Add query parameterization validation

---

### Phase 6: Testing & Documentation (Week 6)

**6.1 Test Coverage Expansion**
Create new test files:
- `tests/unit/test_error_hierarchy.py` - Test all error classes
- `tests/unit/test_retry_policy.py` - Test retry logic
- `tests/unit/test_input_validation.py` - Test validators
- `tests/integration/test_audit_logging.py` - Test audit system
- `tests/security/test_secret_handling.py` - Test secret management
- `tests/performance/test_connection_pool.py` - Test DB pool

**6.2 Documentation Updates**
Update documentation files:
- `docs/SECURITY.md` - Security features and audit logging
- `docs/OBSERVABILITY.md` - Metrics and monitoring
- `docs/DATABASE.md` - Database layer documentation
- `docs/ERROR_HANDLING.md` - Error hierarchy reference

---

## Key Files to Modify

| File | Lines | Changes |
|------|-------|---------|
| `friday_ai/utils/errors.py` | 1-50 | Complete rewrite with error hierarchy |
| `friday_ai/agent/autonomous_loop.py` | 358-512 | Add metrics to CircuitBreaker |
| `friday_ai/tools/registry.py` | 1-200 | Add instrumentation |
| `friday_ai/tools/builtin/database.py` | 1-374 | Add timeouts and pooling |
| `friday_ai/tools/builtin/http_request.py` | 1-209 | Add retry logic |
| `friday_ai/utils/text.py` | 1-50 | Enhance secret scrubbing |
| `friday_ai/config/config.py` | 23-51 | Secret resolution |

## New Files to Create

```
friday_ai/
├── security/
│   ├── __init__.py
│   ├── audit_logger.py
│   ├── secret_manager.py
│   └── validators.py
├── resilience/
│   ├── __init__.py
│   ├── retry.py
│   └── health_checks.py
├── observability/
│   ├── __init__.py
│   ├── metrics.py
│   ├── tracing.py
│   └── logging_config.py
└── database/
    ├── __init__.py
    ├── pool.py
    └── migrations.py
```

## Success Criteria

- **Reliability**: 99.9% uptime, graceful degradation
- **Security**: No high/critical vulnerabilities, full audit trail
- **Performance**: Tool execution < 5s (p95), DB queries < 100ms (p95)
- **Quality**: Test coverage > 90%, zero critical bugs

## Verification Steps

1. Run full test suite: `python -m pytest tests/ -v --cov`
2. Verify audit logging: Check `~/.config/friday/audit.log`
3. Test circuit breaker: Simulate failures, verify state transitions
4. Test retry logic: Disconnect network, verify exponential backoff
5. Run security scan: `bandit -r friday_ai/`
6. Check metrics: `curl http://localhost:8080/metrics`
