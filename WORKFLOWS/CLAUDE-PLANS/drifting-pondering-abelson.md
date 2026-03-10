# Friday AI Teammate v3.0 - Comprehensive Upgrade Plan

## Context

**Current State:** Friday AI Teammate v1.0 is production-ready with 28,105 LOC across 145 Python files. v2.0 features (multi-provider LLM, autonomous goals, swarm mode, RAG, voice I/O, Kubernetes) are implemented but uncommitted.

**User Request:** Create comprehensive upgrade plan improving all features, optimizing folder structure, updating tech stack, achieving 90%+ test coverage, and leveraging skills/MCP/UI-UX best practices.

**Why This Matters:** The project has outgrown its current structure. Session class has 8+ responsibilities, main.py is 1,184 lines, test coverage is only 60-70%, and v2.0 features need integration. This upgrade transforms Friday from a CLI tool to an enterprise-grade AI platform.

---

## Exploration Findings

### Architecture Strengths
- Event-driven design with clean domain separation
- Tool registry pattern with dynamic discovery
- Comprehensive error hierarchy (20+ error classes in `friday_ai/utils/errors.py`)
- Async/await throughout
- Session-oriented with persistence

### Architecture Weaknesses
- **Session class coupling** (`friday_ai/agent/session.py`) - manages 8+ concerns
- **Large files**: `main.py` (1,184 lines), `autonomous_loop.py` (976 lines)
- **Context compaction** is naive (token-based only)
- **No dependency injection** - manual wiring everywhere
- **Mixed validation patterns** scattered across codebase

### Test Coverage Gaps
- **Current**: 60-70% (19 test files, 61+ test functions)
- **Missing**: E2E tests, security tests, API integration tests, performance tests
- **Present**: Unit tests for tools, autonomous mode, claude integration

### UI/UX Status
- Rich terminal UI with 22 custom styles (excellent)
- Voice I/O implemented but **not activated** in main CLI
- Streaming infrastructure exists but simulates token streaming
- No accessibility support (colorblind mode, high contrast)

---

## Phase 1: Foundation (v2.1) - Stabilize & Integrate
**Duration**: 3-4 weeks
**Goal**: Integrate v2.0 features, achieve 80% test coverage, refactor critical paths

### 1.1 Commit v2.0 Features (Week 1)

**Uncommitted Files (20 files):**
```
friday_ai/client/providers/          # Multi-provider (7 files)
friday_ai/client/multi_provider.py    # Smart router
friday_ai/agent/autonomous/           # Goals + self-healing (2 files)
friday_ai/agent/swarm/                # Swarm coordinator
friday_ai/intelligence/               # RAG system (2 files)
friday_ai/ui/voice.py                 # Voice I/O
friday_ai/devops/kubernetes.py        # K8s client
friday_ai/tools/mcp/mcp_registry.py   # 15+ MCP servers
friday_ai/tools/mcp/mcp_installer.py  # Auto-install
friday_ai/claude_integration/skills/  # Skills v2 (2 files)
tests/test_multi_provider.py          # Provider tests
tests/test_mcp.py                     # MCP tests
```

**Actions:**
1. Create feature branch `feature/v2.0-integration`
2. Commit all v2.0 files with conventional commits
3. Update `pyproject.toml` version to `2.1.0`
4. Create comprehensive PR

### 1.2 Session Class Refactoring (Week 1-2)

**Current Problem:** `friday_ai/agent/session.py` manages 8+ concerns

**Solution:** Extract into focused components using composition

**New Classes to Create:**
- `friday_ai/agent/tool_orchestrator.py` (NEW, ~150 lines) - Tool registry, MCP, discovery
- `friday_ai/agent/safety_manager.py` (NEW, ~100 lines) - Approval, validation, sanitization
- `friday_ai/agent/session_metrics.py` (NEW, ~80 lines) - Stats tracking

**Modified Files:**
- `friday_ai/agent/session.py` (92 → ~50 lines) - Simplified orchestration

**Implementation:**
```python
class Session:
    def __init__(self, config: Config):
        self.config = config
        # Delegated components
        self.llm_provider = ProviderManager()
        self.tool_orchestrator = ToolOrchestrator(config)
        self.context_manager = ContextManager(config)
        self.safety_manager = SafetyManager(config)
        self.persistence = SessionPersistence(session_id)
```

### 1.3 Context Compaction Optimization (Week 2)

**Current Problem:** Naive token-based compaction

**Solution:** Multi-strategy compaction with relevance scoring

**New File:** `friday_ai/context/strategies.py` (~200 lines)

**Strategies:**
- `TOKEN_BASED` - Current approach
- `RELEVANCE` - Score by relevance to current query
- `IMPORTANCE` - Tool calls > chit-chat
- `HYBRID` - Combine multiple strategies

**Enhanced File:** `friday_ai/context/compaction.py` - Add strategy selection

### 1.4 Test Coverage Expansion (Week 2-3)

**Target:** 60% → 80% coverage

**New Test Files:**
```
tests/test_providers/           # Multi-provider tests
├── test_openai_provider.py
├── test_anthropic_provider.py
├── test_provider_router.py
└── test_cost_estimation.py

tests/test_autonomous/          # Autonomous enhancement tests
├── test_goal_parser.py
├── test_goal_tracker.py
├── test_self_healing.py
└── test_swarm_coordinator.py

tests/test_intelligence/        # RAG system tests
├── test_rag_indexing.py
├── test_rag_query.py
└── test_chunking.py

tests/test_ui/                  # Voice I/O tests
├── test_voice_input.py
└── test_voice_output.py

tests/test_devops/              # Kubernetes tests
└── test_k8s_client.py
```

**Test Infrastructure:**
- Add `pytest-cov` with 80% minimum threshold
- Add `pytest-benchmark` for performance tests
- Configure `.coveragerc`

### 1.5 Dependency Management (Week 3)

**Update `pyproject.toml`:**
```toml
[project]
requires-python = ">=3.11"  # Upgrade from 3.10

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-cov>=4.1.0",          # NEW
    "pytest-benchmark>=4.0.0",    # NEW
    "black>=24.1.0",              # NEW
    "ruff>=0.2.0",                # NEW (replaces flake8)
    "mypy>=1.8.0",                # NEW
]

rag = [
    "sentence-transformers>=2.2.0",  # NEW
    "faiss-cpu>=1.7.4",              # NEW
]

k8s = ["kubernetes>=28.1.0"]         # NEW

voice = [
    "SpeechRecognition>=3.10.0",     # NEW
    "pyttsx3>=2.90",                 # NEW
    "gTTS>=2.4.0",                   # NEW
]
```

**Add Code Quality Tools:**
```toml
[tool.black]
line-length = 100
target-version = ['py311']

[tool.ruff]
line-length = 100
select = ["E", "F", "I", "N", "W", "UP"]

[tool.mypy]
python_version = "3.11"
strict = true

[tool.pytest.ini_options]
addopts = "--cov=friday_ai --cov-report=term-missing --cov-fail-under=80"
```

### 1.6 Documentation Updates (Week 3)

**Files to Update:**
- `CLAUDE.md` - Add v2.1 features (multi-provider, voice, RAG, K8s)
- `docs/USER-GUIDE.md` - New sections for voice commands, provider switching
- `README.md` - Update features list

**New Documentation:**
- `docs/ARCHITECTURE.md` - System architecture diagram
- `docs/CONTRIBUTING.md` - Development setup, code style, PR workflow

### 1.7 CI/CD Pipeline Setup (Week 4)

**GitHub Actions Workflows:**

`.github/workflows/test.yml`:
- Run on push and PR
- Test Python 3.11 and 3.12
- Run black, ruff, mypy
- Run pytest with coverage
- Upload to Codecov

`.github/workflows/publish.yml`:
- Publish to PyPI on release
- Build and upload with twine

### 1.8 Voice I/O Activation (Week 4)

**Current Status:** Implemented but disabled

**Actions:**
1. Add `/voice` command to main.py
2. Add voice toggle in TUI
3. Handle missing dependencies gracefully
4. Document voice setup in USER-GUIDE.md

---

## Phase 2: Enhancement (v2.5) - Optimize & Extend
**Duration**: 4-6 weeks
**Goal**: Architecture optimization, folder restructure, 90% coverage, plugin system

### 2.1 Folder Structure Optimization (Week 5-6)

**New Structure:**
```
friday_ai/
├── core/                    # Core abstractions (NEW)
│   ├── types.py            # Shared types
│   ├── protocols.py        # Interfaces
│   └── exceptions.py       # Error hierarchy (move from utils/)
│
├── agent/                  # Agent orchestration
│   ├── session.py          # Simplified (50 lines)
│   ├── autonomous/
│   └── orchestration/      # NEW: Orchestration logic
│
├── providers/              # LLM providers (renamed from client/)
│   ├── base.py
│   ├── openai.py
│   ├── anthropic.py
│   ├── google.py
│   ├── groq.py
│   ├── ollama.py
│   └── router.py          # Smart routing
│
├── tools/                  # Tool system
│   ├── builtin/
│   ├── external/          # NEW: External tools
│   │   ├── mcp/
│   │   ├── kubernetes/
│   │   └── cloud/
│   └── registry.py
│
├── plugins/                # NEW: Plugin system
│   ├── base.py            # Plugin interface
│   ├── loader.py          # Plugin discovery
│   └── registry.py        # Plugin registry
│
├── intelligence/           # RAG & knowledge
│   ├── rag.py
│   ├── embeddings.py      # NEW
│   └── knowledge_base.py  # NEW
│
├── storage/                # NEW: Data persistence
│   ├── database.py
│   ├── cache.py
│   └── files.py
│
├── observability/          # Monitoring
│   ├── metrics.py
│   ├── tracing.py         # NEW: Distributed tracing
│   └── logging.py         # NEW: Structured logging
│
└── main.py                 # Simplified (300 lines)
```

**Migration Strategy:**
1. Create new directories
2. Move files incrementally (one module at a time)
3. Update imports with deprecation warnings
4. Update tests
5. Verify with full test suite

### 2.2 Main.py Refactoring (Week 5-6)

**Current Problem:** 1,184 lines of monolithic CLI logic

**Solution:** Extract into focused modules

**New Files:**
- `friday_ai/cli/commands/` directory with separate command modules
  - `session_commands.py` - /save, /resume, /checkpoint
  - `autonomous_commands.py` - /autonomous, /loop
  - `provider_commands.py` - /provider, /cost
  - `tool_commands.py` - /tools, /mcp
  - `config_commands.py` - /config, /model
  - `skills_commands.py` - /skills, /agents
  - `dev_commands.py` - /debug, /profile
- `friday_ai/cli/repl.py` (~200 lines) - Interactive loop
- `friday_ai/cli/parser.py` (~100 lines) - Argument parsing

**Result:** `main.py` reduced to ~300 lines

### 2.3 Dependency Injection System (Week 7)

**New File:** `friday_ai/core/container.py` (~150 lines)

**Implementation:**
```python
class Container:
    def register_singleton(self, interface: type, factory: Callable)
    def resolve(self, interface: type) -> Any

# Usage
container = Container()
container.register_singleton(Config, lambda c: Config.load())
container.register_singleton(ProviderManager, lambda c: ProviderManager(c.resolve(Config)))
```

**Benefits:**
- Cleaner dependency management
- Easier testing with mock injection
- Better separation of concerns

### 2.4 Plugin System (Week 7-8)

**New Files:**
- `friday_ai/plugins/base.py` (~100 lines) - Plugin interface
- `friday_ai/plugins/loader.py` (~150 lines) - Plugin discovery
- `friday_ai/plugins/registry.py` (~100 lines) - Plugin management

**Plugin Interface:**
```python
class FridayPlugin(ABC):
    @property
    @abstractmethod
    def name(self) -> str: pass

    @abstractmethod
    def initialize(self, container: Container) -> None: pass

    def register_tools(self, registry: ToolRegistry) -> None: pass
    def register_commands(self, registry: CommandRegistry) -> None: pass
    def register_providers(self, manager: ProviderManager) -> None: pass
```

**Benefits:**
- Third-party extensions without core changes
- Community contributions
- Modular feature additions

### 2.5 Test Coverage to 90% (Week 8-9)

**New Test Categories:**

**E2E Tests** (`tests/e2e/`):
- `test_cli_workflows.py` - Complete autonomous workflows
- `test_session_persistence.py` - Save/resume workflows
- `test_api_workflows.py` - API session lifecycle

**Performance Tests** (`tests/performance/`):
- `test_context_compaction.py` - Benchmark with 100k tokens
- `test_tool_execution.py` - Throughput benchmarks

**Security Tests** (`tests/security/`):
- `test_injection.py` - SQL injection, path traversal
- `test_secrets.py` - Secret scrubbing verification

**Contract Tests** (`tests/contracts/`):
- `test_provider_interface.py` - All providers implement BaseProvider
- `test_tool_interface.py` - All tools implement Tool protocol

### 2.6 Performance Optimization (Week 9-10)

**Targets:**
- Startup time: <500ms cold start
- Context compaction: <100ms for 50k tokens
- Tool execution: <50ms dispatch overhead

**Strategies:**
- Lazy loading of non-critical components
- Registry caching
- Incremental compaction
- Async parallel execution

### 2.7 Observability Enhancement (Week 10)

**New Files:**
- `friday_ai/observability/tracing.py` (~200 lines) - Distributed tracing
- `friday_ai/observability/logging.py` (~100 lines) - Structured logging

**Features:**
- Span-based tracing with trace IDs
- Export to Jaeger/Zipkin
- Structured JSON logging
- Request/response logging

---

## Phase 3: Innovation (v3.0) - Next-Gen Features
**Duration**: 6-8 weeks
**Goal**: Advanced AI features, production hardening, enterprise readiness

### 3.1 Multi-Modal Support (Week 11-12)

**New File:** `friday_ai/providers/multimodal.py` (~300 lines)

**Features:**
- Vision models (GPT-4V, Claude 3, Gemini Pro Vision)
- Audio transcription (Whisper)
- Image generation (DALL-E 3)

### 3.2 Code Execution Sandbox (Week 12-13)

**New File:** `friday_ai/tools/sandbox.py` (~250 lines)

**Features:**
- Secure Python/JavaScript execution
- Isolated containers
- Resource limits
- Network isolation

### 3.3 AI-Powered Code Review (Week 13-14)

**New File:** `friday_ai/intelligence/code_review.py` (~200 lines)

**Features:**
- Security analysis
- Performance review
- Style consistency
- Best practices suggestions

### 3.4 Production Hardening (Week 14-15)

**Enhanced Files:**
- `friday_ai/resilience/rate_limiter.py` - Adaptive rate limiting
- `friday_ai/resilience/circuit_breaker.py` - Full circuit breaker pattern
- `friday_ai/resilience/fallback.py` (NEW, ~150 lines) - Fallback chains

**Features:**
- Adaptive rate limits based on API responses
- Circuit breaker with half-open state
- Graceful degradation chains

### 3.5 Enterprise Features (Week 15-16)

**New Files:**
- `friday_ai/auth/rbac.py` (~200 lines) - Role-based access control
- `friday_ai/security/audit.py` (ENHANCE) - Comprehensive audit logging
- `friday_ai/security/secrets.py` (ENHANCE) - Enterprise secrets managers

**Features:**
- RBAC with roles (admin, developer, viewer)
- Tamper-evident audit logs
- HashiCorp Vault, AWS Secrets Manager integration

### 3.6 Cloud Deployment (Week 17-18)

**New Files:**
- `Dockerfile` (ENHANCE) - Optimized multi-stage build
- `k8s/deployment.yaml` (NEW) - Kubernetes manifests
- `k8s/service.yaml` (NEW) - Load balancer service
- `k8s/configmap.yaml` (NEW) - Configuration

**Features:**
- Docker optimization with health checks
- Kubernetes deployment with autoscaling
- Ingress configuration
- Secret management

---

## Verification & Testing

### Phase 1 (v2.1) Verification
```bash
# Run full test suite with coverage
pytest --cov=friday_ai --cov-report=html

# Verify 80%+ coverage
coverage report | grep TOTAL

# Test multi-provider
friday
> /provider anthropic
> Hello, Claude!

# Test voice
> /voice on
> [Speak your message]

# Test RAG
> /index ./src
> What does the UserManager class do?

# Run code quality tools
black --check friday_ai tests
ruff check friday_ai tests
mypy friday_ai
```

### Phase 2 (v2.5) Verification
```bash
# Verify folder structure
find friday_ai -type d | head -20

# Verify main.py is simplified
wc -l friday_ai/main.py  # Should be ~300 lines

# Test plugin system
cd plugins/example && python -c "from plugin import Plugin; print(Plugin().name)"

# Run performance benchmarks
pytest tests/performance/ -v

# Verify 90%+ coverage
coverage report | grep TOTAL

# Test distributed tracing
curl http://localhost:8000/trace/123
```

### Phase 3 (v3.0) Verification
```bash
# Test multi-modal
friday
> /upload image.png
> What's in this image?

# Test code sandbox
> /sandbox python
>>> import os
>>> os.system('rm -rf /')  # Should fail safely

# Test Kubernetes deployment
kubectl apply -f k8s/
kubectl get pods

# Test RBAC
curl -H "Authorization: Bearer viewer-token" http://localhost:8000/admin
# Should return 403 Forbidden

# Run full E2E test suite
pytest tests/e2e/ -v
```

---

## Success Criteria

### Phase 1 (v2.1)
- ✅ All v2.0 features committed and integrated
- ✅ Test coverage ≥ 80%
- ✅ Zero critical bugs
- ✅ Documentation updated
- ✅ CI/CD pipeline operational
- ✅ Code quality tools configured (black, ruff, mypy)

### Phase 2 (v2.5)
- ✅ Folder structure optimized
- ✅ main.py refactored (<400 lines)
- ✅ Dependency injection system operational
- ✅ Plugin system working
- ✅ Test coverage ≥ 90%
- ✅ Performance benchmarks passing
- ✅ Observability enhanced (tracing, structured logging)

### Phase 3 (v3.0)
- ✅ Multi-modal support operational
- ✅ Code sandbox functional
- ✅ Production hardening complete
- ✅ Enterprise features available
- ✅ Cloud deployment ready
- ✅ Full documentation

---

## Risk Mitigation

**Breaking Changes:**
- Maintain backward compatibility layer
- Auto-migration scripts for configs
- Deprecation warnings before removal
- Comprehensive migration guide

**Performance Regression:**
- Benchmark suite in CI
- Performance testing on every PR
- Profiling in production (optional)

**Test Coverage Gaps:**
- Mutation testing
- Code coverage enforcement in CI
- Regular test audits

**Dependency Conflicts:**
- Pin dependency versions
- Regular dependency updates
- Security scanning (Dependabot)

---

## Timeline Summary

**Phase 1 (v2.1):** 3-4 weeks
- Week 1: Commit v2.0, start Session refactoring
- Week 2: Complete refactoring, context optimization
- Week 3: Test expansion, dependencies
- Week 4: Documentation, CI/CD, voice activation

**Phase 2 (v2.5):** 4-6 weeks
- Week 5-6: Folder restructure, main.py refactoring
- Week 7-8: DI system, plugin system
- Week 9-10: Test coverage to 90%, performance, observability

**Phase 3 (v3.0):** 6-8 weeks
- Week 11-14: Multi-modal, sandbox, AI review
- Week 15-16: Production hardening, enterprise features
- Week 17-18: Cloud deployment, final testing

**Total Duration:** 13-18 weeks (~4-5 months)

---

## Critical Files to Modify/Create

**Phase 1 (v2.1):**
- `friday_ai/agent/session.py` - Refactor (92 → 50 lines)
- `friday_ai/agent/tool_orchestrator.py` - NEW (~150 lines)
- `friday_ai/agent/safety_manager.py` - NEW (~100 lines)
- `friday_ai/context/strategies.py` - NEW (~200 lines)
- `pyproject.toml` - Update dependencies and tools

**Phase 2 (v2.5):**
- `friday_ai/main.py` - Refactor (1,184 → 300 lines)
- `friday_ai/cli/` - NEW directory with command modules
- `friday_ai/core/container.py` - NEW DI system (~150 lines)
- `friday_ai/plugins/` - NEW plugin system (3 files)

**Phase 3 (v3.0):**
- `friday_ai/providers/multimodal.py` - NEW (~300 lines)
- `friday_ai/tools/sandbox.py` - NEW (~250 lines)
- `friday_ai/intelligence/code_review.py` - NEW (~200 lines)
- `friday_ai/auth/rbac.py` - NEW (~200 lines)
- `k8s/` - NEW deployment manifests

---

## Next Steps

1. **Immediate:** Review and approve this plan
2. **Week 1:** Create feature branch, commit v2.0 features
3. **Week 1-2:** Begin Session class refactoring
4. **Week 2-3:** Expand test coverage
5. **Iterate:** Follow phased approach with continuous testing

This plan transforms Friday AI Teammate from a CLI assistant to an enterprise-grade AI development platform while maintaining backward compatibility and code quality.
