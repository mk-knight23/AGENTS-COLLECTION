# Friday AI v0.3.0 - Comprehensive Application Upgrade Plan

## Context

This upgrade aims to fully integrate the patterns and best practices from the `.claude` folder (agents, skills, commands, rules), `docs` folder (documentation standards), and `ralph-claude-code` (autonomous development patterns) into the Friday AI application.

**Current State:**
- Version: 0.2.0 (pyproject.toml shows 0.2.0, main.py shows 0.3.0 - needs alignment)
- Core features: Agent system, tools, MCP support, basic autonomous loop, session management
- Has .claude folder integration but incomplete

**Target State:**
- Version: 0.3.0 (unified)
- Full Ralph-inspired autonomous loop with circuit breaker, rate limiting, response analysis
- Complete .claude folder integration (agents, skills, commands, workflows)
- Enhanced documentation
- Improved CLI with all commands functional

---

## Phase 1: Core Fixes and Alignment

### 1.1 Version Alignment
**File:** `friday_ai/main.py` (line 23), `pyproject.toml` (line 7)
**Change:** Align versions to 0.3.0
**Rationale:** Current inconsistency between main.py (0.3.0) and pyproject.toml (0.2.0)

### 1.2 Fix Autonomous Loop Integration
**File:** `friday_ai/main.py` (lines 542-609)
**Issues:**
- `AutonomousLoop` is instantiated but `agent` is not properly initialized
- The loop needs agent to be fully initialized with session
- Missing proper async context handling

**Fix:**
```python
# In _start_autonomous_loop, ensure agent is properly initialized
if not self.agent:
    self.agent = Agent(self.config)
    await self.agent.__aenter__()
```

---

## Phase 2: Enhance Autonomous Loop (Ralph Patterns)

### 2.1 Enhance ResponseAnalyzer
**File:** `friday_ai/agent/autonomous_loop.py` (lines 96-171)
**Additions:**
- JSON response parsing (like Ralph's parse_json_response)
- Permission denial detection
- Session ID extraction from responses
- Two-stage error filtering (eliminate false positives from JSON fields)
- Multi-line error matching for stuck loop detection

**New Methods:**
- `parse_json_response()` - Extract structured data from Claude JSON output
- `extract_session_id()` - Get session ID for continuity
- `filter_false_positive_errors()` - Two-stage error filtering

### 2.2 Enhance Circuit Breaker
**File:** `friday_ai/agent/autonomous_loop.py` (lines 174-241)
**Additions:**
- Permission denial threshold (Issue #101 from Ralph)
- Output decline detection
- Better state transitions with HALF_OPEN support
- History tracking for circuit breaker events

### 2.3 Add Session Continuity to Autonomous Loop
**File:** `friday_ai/agent/autonomous_loop.py`
**Additions:**
- Session persistence across loop iterations
- `--continue` flag support
- Session expiration handling (24 hours)
- Session history tracking

### 2.4 Add Status File Updates
**File:** `friday_ai/agent/autonomous_loop.py`
**Additions:**
- Real-time status.json updates during loop execution
- Log file generation per iteration
- Progress tracking

---

## Phase 3: Complete .claude Integration

### 3.1 Fix Command Mapper
**File:** `friday_ai/claude_integration/command_mapper.py`
**Action:** Ensure all commands from `.claude/commands/` are properly loaded and executable

### 3.2 Fix Agent Loader
**File:** `friday_ai/claude_integration/agent_loader.py`
**Action:** Ensure agents can be invoked via `/agents` command and used in workflows

### 3.3 Fix Skills Manager
**File:** `friday_ai/claude_integration/skills_manager.py`
**Action:** Ensure skills can be activated and their patterns applied

### 3.4 Fix Workflow Engine
**File:** `friday_ai/claude_integration/workflow_engine.py`
**Action:** Ensure workflows can be executed with proper step orchestration

### 3.5 Add Missing Commands Implementation
**File:** `friday_ai/main.py` (lines 611-692)
**Issues:**
- `_control_loop` has TODO comments (stop, pause, resume not implemented)
- `_control_circuit_breaker` has TODO comments
- Need actual state management for loop control

---

## Phase 4: Enhanced CLI Commands

### 4.1 Implement Loop Control Commands
**Commands to implement:**
- `/loop stop` - Stop the autonomous loop gracefully
- `/loop pause` - Pause the loop
- `/loop resume` - Resume the loop
- `/loop status` - Show detailed loop status

### 4.2 Implement Circuit Breaker Commands
**Commands to implement:**
- `/circuit reset` - Reset circuit breaker to CLOSED
- `/circuit open` - Manually open circuit breaker
- `/circuit close` - Close circuit breaker
- `/circuit status` - Show circuit breaker state and history

### 4.3 Add Missing Commands from .claude/commands/
**Commands to add:**
- `/plan` - Use planner agent
- `/tdd` - Use TDD workflow
- `/code-review` - Use code reviewer agent
- `/go-test` - Run Go tests with coverage
- `/go-build` - Fix Go build errors
- `/test-coverage` - Check test coverage
- `/refactor-clean` - Clean up dead code
- `/update-docs` - Update documentation
- `/update-codemaps` - Update codemaps

---

## Phase 5: Documentation Updates

### 5.1 Update CLAUDE.md
**File:** `docs/CLAUDE.md`
**Add:**
- Autonomous loop documentation
- Session management details
- .claude integration patterns
- New CLI commands reference

### 5.2 Create AUTONOMOUS-MODE.md
**File:** `docs/AUTONOMOUS-MODE.md`
**Content:**
- How to use `/autonomous` command
- Configuration options
- Exit conditions
- Circuit breaker behavior
- Rate limiting details

### 5.3 Create SESSION-MANAGEMENT.md
**File:** `docs/SESSION-MANAGEMENT.md`
**Content:**
- Session lifecycle
- Persistence mechanism
- Resume functionality
- Expiration handling

### 5.4 Update UPGRADE-v0.3.0.md
**File:** `docs/UPGRADE-v0.3.0.md`
**Content:**
- Migration guide from v0.2.0
- New features list
- Breaking changes (if any)

---

## Phase 6: Testing and Validation

### 6.1 Run Existing Tests
**Command:** `pytest tests/ -v`
**Ensure:** All existing tests pass

### 6.2 Add New Tests
**Files:**
- `tests/test_autonomous_loop.py` - Test autonomous loop functionality
- `tests/test_circuit_breaker.py` - Test circuit breaker states
- `tests/test_response_analyzer.py` - Test response analysis
- `tests/test_session_manager.py` - Test session management

---

## Phase 7: Add Missing Tools

### 7.1 HTTP Request Tool
**File:** `friday_ai/tools/builtin/http_request.py`
**Status:** Exists but verify it has all needed features

### 7.2 Database Tool
**File:** `friday_ai/tools/builtin/database.py`
**Status:** Exists but verify functionality

### 7.3 Docker Tool
**File:** `friday_ai/tools/builtin/docker.py`
**Status:** Exists but verify functionality

### 7.4 Git Tool
**File:** `friday_ai/tools/builtin/git.py`
**Status:** Exists but verify functionality

---

## Critical Files to Modify

| File | Lines | Changes |
|------|-------|---------|
| `friday_ai/main.py` | 1138 | Fix autonomous loop integration, implement TODOs, add commands |
| `friday_ai/agent/autonomous_loop.py` | 512 | Enhance response analysis, circuit breaker, session continuity |
| `friday_ai/agent/session_manager.py` | 415 | Add session history, better lifecycle management |
| `friday_ai/claude_integration/command_mapper.py` | ~100 | Fix command loading and execution |
| `friday_ai/claude_integration/workflow_engine.py` | ~150 | Fix workflow execution |
| `pyproject.toml` | 69 | Update version |
| `docs/CLAUDE.md` | 158 | Update documentation |
| `docs/UPGRADE-v0.3.0.md` | New | Create migration guide |
| `docs/AUTONOMOUS-MODE.md` | New | Create autonomous mode guide |
| `docs/SESSION-MANAGEMENT.md` | New | Create session management guide |

---

## Verification Steps

1. **Version Check:**
   ```bash
   friday --version
   # Should show: Friday AI Teammate v0.3.0
   ```

2. **Configuration Check:**
   ```bash
   friday --config
   # Should show all configuration options
   ```

3. **Autonomous Loop Test:**
   ```bash
   friday
   > /autonomous
   # Should start autonomous loop with proper prompts
   ```

4. **Command Tests:**
   ```bash
   friday
   > /claude
   # Should show .claude integration status
   > /agents
   # Should list available agents
   > /skills
   # Should list available skills
   ```

5. **Session Management Test:**
   ```bash
   friday
   > /save
   # Should save session
   > /sessions
   # Should list sessions
   ```

6. **Run Tests:**
   ```bash
   pytest tests/ -v
   # All tests should pass
   ```

---

## Risks and Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| Breaking existing functionality | High | Comprehensive testing, phased rollout |
| Async issues in autonomous loop | Medium | Proper async context management |
| Session data corruption | Medium | Backup/restore mechanism |
| Performance degradation | Low | Profiling and optimization |

---

## Timeline Estimate

| Phase | Duration |
|-------|----------|
| Phase 1: Core Fixes | 30 min |
| Phase 2: Autonomous Loop | 1 hour |
| Phase 3: .claude Integration | 45 min |
| Phase 4: CLI Commands | 45 min |
| Phase 5: Documentation | 30 min |
| Phase 6: Testing | 30 min |
| Phase 7: Tools | 30 min |
| **Total** | **~4.5 hours** |

---

## Dependencies

- All changes are within the existing codebase
- No new external dependencies required
- Uses patterns from ralph-claude-code (which is already in the repo)

---

*Plan created: 2026-02-09*
*Target version: 0.3.0*
