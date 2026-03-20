# 🚀 AGENTS-COLLECTION (Collective Production Edition)

## 💎 Overview
Fully production-grade implementation of AGENTS-COLLECTION, refactored by the **69-Agent Opencode Collective**.

## 🛡️ Trust & Compliance
- **CI/CD**: Automated GitHub Actions with Gitleaks security scans.
- **Security**: Standardized [SECURITY.md](SECURITY.md) protocol.
- **Design**: Opencode Premium Design Tokens integrated.

## 🏁 48-Hour Roadmap
1. Initialize infrastructure via `.github/workflows`.
2. Set your secrets in GitHub Environment settings.
3. Deploy to production via Vercel/Docker.

# 🤖 AGENTS-COLLECTION

### The Most Comprehensive AI Agent Library on the Planet

**A unified archive of AI agent definitions, skills, prompts, and configurations**
**collected, converted, and deployed across 11 AI coding platforms.**

---

[![Agents](https://img.shields.io/badge/AGENTS-700%2B-blueviolet?style=for-the-badge&logo=robot)](#-agents)
[![Skills](https://img.shields.io/badge/SKILLS-860%2B-blue?style=for-the-badge&logo=lightning)](#-skills)
[![Prompts](https://img.shields.io/badge/PROMPTS-141-orange?style=for-the-badge&logo=chat)](#-prompts)
[![Platforms](https://img.shields.io/badge/PLATFORMS-11-green?style=for-the-badge&logo=grid)](#-platform-coverage)
[![Files](https://img.shields.io/badge/FILES-2%2C700%2B-red?style=for-the-badge&logo=files)](#-repository-structure)
[![License](https://img.shields.io/badge/LICENSE-MIT-yellow?style=for-the-badge&logo=law)](LICENSE)

</div>

---

## 📖 TABLE OF CONTENTS

| # | Section |
|---|---------|
| 1 | [What Is This?](#-what-is-this) |
| 2 | [Platform Coverage](#-platform-coverage) |
| 3 | [Repository Structure](#-repository-structure) |
| 4 | [File Type Breakdown](#-file-type-breakdown) |
| 5 | [Agents](#-agents) |
| 6 | [Skills](#-skills) |
| 7 | [Prompts](#-prompts) |
| 8 | [Plugins, MCP, Hooks, Configs](#-plugins--mcp--hooks--configs) |
| 9 | [The 68 Core Agency Agents](#-the-68-core-agency-agents) |
| 10 | [How To Use](#-how-to-use) |
| 11 | [References & Source Repos](#-references--source-repos) |
| 12 | [Credits & Contributions](#-credits--contributions) |

---

## 🧠 WHAT IS THIS?

This repository is a **living snapshot** of an AI-native development environment — every agent definition, skill file, prompt, workflow, MCP server config, hook, plugin, and platform config collected from a single power-user's machine across **11 AI coding assistants**.

**Core value propositions:**
- 🔍 **Discover** — Browse 700+ unique agent definitions in one place
- 🔄 **Cross-platform** — See how the same agent is expressed in 6+ different formats
- 🚀 **Deploy** — Copy any folder directly into your own tool's config directory
- 📚 **Learn** — Study agent design patterns, skill structures, and prompt engineering at scale

---

## 🖥️ PLATFORM COVERAGE

| Platform | Type | Agents/Skills | Source Folder | Global Config Path |
|----------|------|:---:|---------------|-------------------|
| **Claude Code** | AI CLI | 129 agents | `AGENTS/CLAUDE-CODE/` | `~/.claude/agents/` |
| **AntiGravity** (Gemini) | AI CLI | 82 skills | `AGENTS/ANTIGRAVITY/SKILLS/` | `~/.gemini/antigravity/skills/` |
| **Cursor** | AI IDE | 68 rules | `AGENTS/CURSOR/` | `~/.cursor/rules/` |
| **OpenCode** | AI Editor | 68 agents | `AGENTS/OPENCODE/` | `~/.config/opencode/agent/` |
| **GitHub Copilot** | AI Pair | 68 agents | `AGENTS/PICOCLAW/` | `~/.github/copilot-instructions.md` |
| **NanoBot** | Agent Runner | 68 skills | `SKILLS/NANOBOT/` | `~/.nanobot/skills/` |
| **NanoClaw** (Claude) | Agent Platform | 89 skills | `SKILLS/NANOCLAW/` | `.claude/skills/` |
| **OpenClaw** | Multi-Agent | 22 agents | `AGENTS/OPENCLAW/` | `.openclaw/agents/` |
| **PicoClaw** (Copilot) | Code Agent | 2 configs | `AGENTS/PICOCLAW/` | `.github/copilot-instructions.md` |
| **ZeroClaw** (Gemini) | Code Agent | 69 prompts | `PROMPTS/ZEROCLAW-GEMINI/` | `.gemini/agents/` |
| **Everything-CC** | Plugin Pack | 13 agents | `AGENTS/EVERYTHING-CC/` | `~/.claude/agents/` |

---

## 📁 REPOSITORY STRUCTURE

```
AGENTS-COLLECTION/
│
├── AGENTS/                        ← Agent definitions by platform
│   ├── CLAUDE-CODE/               │   129 .md files — global Claude Code agents
│   ├── ANTIGRAVITY/               │   AntiGravity (Gemini CLI) data
│   │   ├── SKILLS/                │   82 skill folders — each with SKILL.md
│   │   ├── ANNOTATIONS/           │   Code annotation data
│   │   ├── RULES/                 │   AntiGravity rule files (.pbtxt)
│   │   └── WORKFLOWS/             │   Workflow definitions
│   ├── CURSOR/                    │   68 .mdc cursor rule files
│   ├── OPENCODE/                  │   68 .md OpenCode agent definitions
│   ├── PICOCLAW/                  │   GitHub Copilot instruction files
│   ├── NANOCLAW/                  │   41 NanoClaw agent files
│   ├── OPENCLAW/                  │   22 multi-agent team configs
│   │   ├── FEATURE-DEV_*/         │   6-agent feature dev team
│   │   ├── BUG-FIX_*/             │   6-agent bug fix team
│   │   └── SECURITY-AUDIT_*/      │   7-agent security team
│   ├── EVERYTHING-CC/             │   13 Everything-Claude-Code agents
│   └── AGENCY-SOURCE/             │   85 source agents (canonical MD)
│       ├── DESIGN/                │   7 design agents
│       ├── ENGINEERING/           │   11 engineering agents
│       ├── MARKETING/             │   8 marketing agents
│       ├── PRODUCT/               │   6 product agents
│       ├── PROJECT-MANAGEMENT/    │   5 PM agents
│       ├── SPECIALIZED/           │   14 specialized agents
│       ├── SPATIAL-COMPUTING/     │   5 XR/spatial agents
│       ├── SUPPORT/               │   5 support agents
│       ├── TESTING/               │   6 testing agents
│       └── STRATEGY/              │   extra strategy agents
│
├── SKILLS/                        ← Installable skills & capabilities
│   ├── CLAUDE-CODE/               │   499 files — SKILL.md + manifests
│   ├── NANOCLAW/                  │   262 files — 89 containerized skills
│   ├── OPENCLAW/                  │
│   │   ├── SRC/                   │   27 files — global OpenClaw skills
│   │   └── PROJECT/               │   74 files — project-level skills
│   ├── NANOBOT/                   │   69 folders — skill.json + SKILL.md
│   └── EVERYTHING-CC/             │   48 files + 51 OpenCode skill configs
│       └── OPENCODE/              │
│
├── PROMPTS/                       ← Prompt collections
│   ├── OPENCLAW-PI/               │   72 Pi prompts (frontmatter .md)
│   └── ZEROCLAW-GEMINI/           │   69 Gemini Code Assist agent files
│
├── PLUGINS/                       ← Plugin manifests & extensions
│   ├── CLAUDE-CODE/               │   500 files — manifests + docs
│   └── OPENCLAW/                  │   9 OpenClaw extension files
│
├── WORKFLOWS/                     ← Workflow definitions & plans
│   ├── CLAUDE-PLANS/              │   8 Claude Code implementation plans
│   └── OPENCLAW/WORKFLOWS/        │   1 OpenClaw workflow definition
│
├── MCP/                           ← MCP server configs (secrets redacted)
│   ├── CLAUDE-CODE/               │   mcp.json + .mcp.json
│   ├── NANOCLAW/                  │   .mcp.json
│   ├── CURSOR/                    │   mcp.json
│   └── OPENCLAW/                  │   MCP configs
│
├── HOOKS/                         ← Pre/post execution hooks
│   ├── CLAUDE-CODE/               │   Claude Code hooks
│   └── OPENCLAW/                  │   OpenClaw hooks
│
├── RULES/                         ← Rule files
│   └── CLAUDE-CODE/               │   .md rule files (coding style, git, etc.)
│
├── DOCS/                          ← Documentation
│   ├── NANOCLAW/                  │   Architecture docs
│   ├── OPENCLAW/                  │   AGENTS.md, CLAUDE.md
│   ├── ZEROCLAW/                  │   AGENTS.md, CLAUDE.md
│   └── PICOCLAW/                  │   19 doc files
│
└── CONFIGS/                       ← Platform configs (secrets redacted)
    ├── CLAUDE-CODE/               │   GEMINI.md
    ├── OPENCLAW/                  │   openclaw.json
    ├── NANOBOT/                   │   config.json
    ├── CURSOR/                    │   mcp.json, cli-config.json
    ├── PICOCLAW/                  │   config.json
    └── ZEROCLAW/                  │   config.toml, zeroclaw.json
```

---

## 📊 FILE TYPE BREAKDOWN

| Extension | Count | Approx Size | Category | Used By |
|-----------|:-----:|:-----------:|----------|---------|
| `.md` | **2,186** | ~8 MB | Agent defs, skills, docs, prompts | All platforms |
| `.json` | **168** | ~3 MB | Configs, manifests, skill.json | NanoBot, NanoClaw, Plugins |
| `.ts` | **122** | ~1.5 MB | TypeScript skill implementations | NanoClaw, Everything-CC |
| `.yaml` | **80** | ~400 KB | Manifests, NanoClaw configs | NanoClaw, OpenClaw |
| `.mdc` | **68** | ~1.5 MB | Cursor rule files | Cursor |
| `.pbtxt` | **19** | ~200 KB | AntiGravity rule/workflow data | AntiGravity |
| `.py` | **16** | ~200 KB | Python skill scripts | NanoClaw |
| `.txt` | **14** | ~100 KB | Text prompts, notes | Various |
| `.mjs` | **13** | ~150 KB | JavaScript modules | Everything-CC |
| `.sh` | **11** | ~50 KB | Shell scripts, installers | Various |
| `.toml` | **1** | ~2 KB | ZeroClaw config | ZeroClaw |
| `Dockerfile` | **2** | ~3 KB | Container skill definitions | NanoClaw |

> **Markdown dominates (80%)** — all platforms converge on `.md` as the universal agent definition format.

> **Excluded from this repo:** 600+ MB of runtime data (.pb conversation files, sessions.json, brain state, code tracking) — only agent *definitions* are committed.

---

## 🤖 AGENTS

### Claude Code — 129 Agents

Global agents at `~/.claude/agents/` covering the full development lifecycle:

<details>
<summary><strong>View all Claude Code agent categories</strong></summary>

| Category | Agents |
|----------|--------|
| **Engineering** | backend-architect, frontend-developer, mobile-app-builder, devops-automator, rapid-prototyper, ai-engineer, security-engineer, data-engineer, senior-developer, technical-writer, autonomous-optimization-architect |
| **Design** | ui-designer, ux-architect, brand-guardian, visual-storyteller, image-prompt-engineer, inclusive-visuals-specialist, whimsy-injector |
| **Marketing** | content-creator, tiktok-strategist, trend-researcher, app-store-optimizer, community-manager, analytics-reporter, campaign-manager, growth-hacker |
| **Product** | product-writer, sprint-prioritizer, feedback-synthesizer, studio-producer, experiment-tracker, project-shipper |
| **Testing** | test-writer-fixer, api-tester, qa-specialist, test-results-analyzer |
| **Support** | customer-support, onboarding-guide, documentation-specialist, knowledge-base-curator, feedback-analyst |
| **Specialized** | joker, nexus-strategy, tool-evaluator, zhihu-strategist, and 40+ more |
| **System (Agency)** | planner, architect, tdd-guide, code-reviewer, security-reviewer, build-error-resolver, e2e-runner, refactor-cleaner, doc-updater |

</details>

### AntiGravity (Gemini CLI) — 82 Skills

Installed at `~/.gemini/antigravity/skills/`. Each skill is a named folder with `SKILL.md`:

```
AGENCY-BACKEND-ARCHITECT/
└── SKILL.md    # name, description, risk_level, source frontmatter
```

Includes all 68 Agency agents + 14 additional GWS recipe skills.

### Agency Source — 68 Canonical Agents

Original [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) definitions in `AGENTS/AGENCY-SOURCE/`:

| Division | Count | Sample Agents |
|----------|:-----:|---------------|
| Engineering | 11 | backend-architect, frontend-developer, devops-automator, ai-engineer |
| Design | 7 | ui-designer, ux-architect, brand-guardian, whimsy-injector |
| Marketing | 8 | content-creator, tiktok-strategist, trend-researcher, app-store-optimizer |
| Product | 6 | product-writer, sprint-prioritizer, feedback-synthesizer, studio-producer |
| Project Mgmt | 5 | studio-coach, experiment-tracker, project-shipper |
| Testing | 6 | test-writer-fixer, api-tester, qa-specialist, e2e-runner |
| Support | 5 | customer-support, documentation-specialist, knowledge-base-curator |
| Spatial Computing | 5 | xr-developer, ar-experience-designer, vr-environment-builder |
| Specialized | 14 | joker, nexus-strategy, tool-evaluator, zhihu-strategist + more |

### OpenClaw Multi-Agent Teams — 22 Configs

`AGENTS/OPENCLAW/` — Production multi-agent team configs:

| Team | Agents | Purpose |
|------|:------:|---------|
| **feature-dev** | 6 | planner → developer → reviewer → tester → verifier → setup |
| **bug-fix** | 6 | triager → investigator → fixer → pr → setup → verifier |
| **security-audit** | 7 | scanner → prioritizer → fixer → tester → verifier → pr → setup |
| **acp / codex / main** | 3 | Orchestration & coordination |

---

## ⚡ SKILLS

### Claude Code Skills — 499 Files

`SKILLS/CLAUDE-CODE/` — The most comprehensive Claude Code skill library:

<details>
<summary><strong>Skill categories (click to expand)</strong></summary>

| Category | Count | Description |
|----------|:-----:|-------------|
| **GWS Skills** | 80+ | Gmail, Drive, Calendar, Sheets, Docs, Slides, Meet, Chat, Classroom, Forms |
| **Persona Skills** | 10 | exec-assistant, researcher, project-manager, customer-support, sales-ops |
| **Recipe Skills** | 50+ | batch-invite, backup-sheet, compare-tabs, draft-from-doc, find-free-time |
| **Agency Skills** | 68 | All 68 Agency agents as installable skills |
| **Code Skills** | 20+ | TDD, review, security, refactor, build-error-resolver, e2e |
| **Everything-CC** | 48 | Battle-tested skills from Everything-Claude-Code |

</details>

### NanoClaw Skills — 262 Files (89 Skill Folders)

`SKILLS/NANOCLAW/` — Docker-based containerized skills:

```
SKILL-NAME/
├── SKILL.md          # Description + manifest
├── manifest.yaml     # NanoClaw manifest
└── MODIFY/
    ├── Dockerfile    # Container definition
    └── SRC/          # Implementation
```

Notable skills: `ADD-PDF-READER`, `USE-LOCAL-WHISPER`, `CONVERT-TO-APPLE-CONTAINER`, `SHERPA-ONNX-TTS`, `ADK-TOOL-SCAFFOLD` + 84 more.

### NanoBot Skills — 69 Folders

`SKILLS/NANOBOT/` — Each folder: `skill.json` + `SKILL.md`:

```json
{
  "name": "agency-backend-architect",
  "description": "Expert backend systems designer",
  "trigger": "design API|architect backend|scale service",
  "model": "claude-sonnet-4-5"
}
```

### Everything-CC Skills — 99 Files

`SKILLS/EVERYTHING-CC/` — From [disler/everything-claude-code](https://github.com/disler/everything-claude-code):

- TDD workflow, code review, security scan, python/go/java review
- Django, SpringBoot, FastAPI, PostgreSQL patterns
- Deployment, Docker, E2E testing, ClickHouse patterns
- Content-hash-cache, eval-harness, iterative-retrieval

---

## 💬 PROMPTS

### OpenClaw Pi Prompts — 72 Files

`PROMPTS/OPENCLAW-PI/` — Frontmatter-based prompts for the Pi intelligence system:

```markdown
---
name: backend-architect
description: Design scalable backend systems
category: engineering
---
[prompt body]
```

### ZeroClaw Gemini Prompts — 69 Files

`PROMPTS/ZEROCLAW-GEMINI/` — Gemini Code Assist compatible agent files:

```markdown
# Backend Architect
> Design scalable APIs and distributed systems

[full agent prompt]
```

---

## 🔌 PLUGINS · MCP · HOOKS · CONFIGS

### Claude Code Plugins — 500 Files

`PLUGINS/CLAUDE-CODE/` — Full plugin manifests + multilingual documentation.
Includes `EVERYTHING-CLAUDE-CODE` plugin cache with 30+ skills in English, Chinese (zh-cn), and Japanese (ja-jp).

### MCP Server Configs *(secrets redacted)*

`MCP/` — Model Context Protocol server configurations:

| File | MCP Servers Configured |
|------|----------------------|
| `CLAUDE-CODE/mcp.json` | filesystem, github, figma, supabase, vercel, railway, cloudflare, firecrawl, memory, sequential-thinking, playwright, web-search, linear, gmail, canva, gamma, indeed, zread, context7 |
| `CLAUDE-CODE/.mcp.json` | Project-level overrides |
| `CURSOR/mcp.json` | Cursor MCP (same 20+ servers) |
| `NANOCLAW/.mcp.json` | NanoClaw project MCP |

> ⚠️ All API tokens, PATs, and secrets replaced with `***REDACTED***` before commit.

### Hooks — 8 Files

`HOOKS/` — Pre/post execution lifecycle hooks:
- Session-start hooks (context loading, memory init)
- Tool-use hooks (validation, auto-format)
- Stop hooks (final verification, cleanup)

### Configs *(secrets redacted)*

`CONFIGS/` — Platform configuration files:

| File | Platform | Notes |
|------|----------|-------|
| `CLAUDE-CODE/GEMINI.md` | Gemini integration | Gemini model config |
| `OPENCLAW/openclaw.json` | OpenClaw platform | Agent team definitions |
| `NANOBOT/config.json` | NanoBot | 20+ LLM provider configs |
| `CURSOR/mcp.json` | Cursor | MCP + tool config |
| `ZEROCLAW/config.toml` | ZeroClaw | Gemini CLI config |
| `PICOCLAW/config.json` | PicoClaw | Copilot config |

---

## 🌟 THE 68 CORE AGENCY AGENTS

All 68 agents from [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) installed across **5 tools** simultaneously in their native formats:

| Agent | Claude Code | Cursor | OpenCode | AntiGravity | Copilot |
|-------|:-----------:|:------:|:--------:|:-----------:|:-------:|
| backend-architect | ✅ `.md` | ✅ `.mdc` | ✅ `.md` | ✅ `SKILL.md` | ✅ concat |
| frontend-developer | ✅ | ✅ | ✅ | ✅ | ✅ |
| mobile-app-builder | ✅ | ✅ | ✅ | ✅ | ✅ |
| devops-automator | ✅ | ✅ | ✅ | ✅ | ✅ |
| rapid-prototyper | ✅ | ✅ | ✅ | ✅ | ✅ |
| ai-engineer | ✅ | ✅ | ✅ | ✅ | ✅ |
| security-engineer | ✅ | ✅ | ✅ | ✅ | ✅ |
| ui-designer | ✅ | ✅ | ✅ | ✅ | ✅ |
| ux-architect | ✅ | ✅ | ✅ | ✅ | ✅ |
| content-creator | ✅ | ✅ | ✅ | ✅ | ✅ |
| tiktok-strategist | ✅ | ✅ | ✅ | ✅ | ✅ |
| product-writer | ✅ | ✅ | ✅ | ✅ | ✅ |
| ... (56 more) | ✅ | ✅ | ✅ | ✅ | ✅ |

**Also installed in NanoBot, NanoClaw, OpenClaw, PicoClaw, ZeroClaw** — 10 platforms total.

Each format differs:

| Platform | File Format | Key Fields |
|----------|-------------|-----------|
| Claude Code | `.md` + YAML frontmatter | `name`, `description`, `model`, `tools` |
| Cursor | `.mdc` | `description`, `globs`, `alwaysApply` |
| OpenCode | `.md` + frontmatter | `name`, `description`, `color` |
| AntiGravity | folder/`SKILL.md` | `name`, `description`, `risk_level`, `source` |
| GitHub Copilot | concat in single `.md` | plain markdown sections |
| NanoBot | `skill.json` + `SKILL.md` | `name`, `description`, `trigger`, `model` |
| NanoClaw | `manifest.yaml` + `SKILL.md` | `name`, `version`, `description` |
| OpenClaw Pi | frontmatter `.md` | `name`, `description`, `category` |
| ZeroClaw | plain `.md` | `# Title` + `> description` |

---

## 🚀 HOW TO USE

### Install — Claude Code Agents
```bash
cp AGENTS/CLAUDE-CODE/*.md ~/.claude/agents/
ls ~/.claude/agents/ | wc -l   # verify
```

### Install — AntiGravity Skills
```bash
cp -r AGENTS/ANTIGRAVITY/SKILLS/* ~/.gemini/antigravity/skills/
```

### Install — Cursor Rules
```bash
cp AGENTS/CURSOR/*.mdc ~/.cursor/rules/
```

### Install — OpenCode Agents
```bash
cp AGENTS/OPENCODE/*.md ~/.config/opencode/agent/
```

### Install — NanoBot Skills
```bash
cp -r SKILLS/NANOBOT/* ~/.nanobot/skills/
```

### Install — NanoClaw Skills
```bash
# Per-project install
cp -r SKILLS/NANOCLAW/ADD-PDF-READER /path/to/project/.claude/skills/
```

### Browse & Search
```bash
# Find agents by topic
grep -rl "security" AGENTS/ --include="*.md" | head -20

# Find skills with specific capability
grep -rl "TypeScript" SKILLS/ --include="*.md" | head -10

# List all agents by platform
ls AGENTS/CLAUDE-CODE/
ls AGENTS/OPENCODE/
ls AGENTS/CURSOR/

# Find duplicate agent definitions across platforms
grep -rh "^name:" AGENTS/ --include="*.md" | sort | uniq -d
```

---

## 🔗 REFERENCES & SOURCE REPOS

### Source Projects

| Project | Author | Link | Contribution |
|---------|--------|------|-------------|
| **agency-agents** | msitarzewski | [github.com/msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 68 canonical agent definitions — the backbone |
| **everything-claude-code** | disler | [github.com/disler/everything-claude-code](https://github.com/disler/everything-claude-code) | 48 skills, 13 agents, OpenCode configs |
| **gemini-cli** | Google | [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | AntiGravity skill platform |
| **NanoClaw** | mk-knight23 | [github.com/mk-knight23/NanoClaw](https://github.com/mk-knight23) | Containerized Claude skill platform |
| **openclaw** | mk-knight23 | [github.com/mk-knight23/openclaw](https://github.com/mk-knight23) | Multi-agent team platform |
| **zeroclaw** | mk-knight23 | [github.com/mk-knight23/zeroclaw](https://github.com/mk-knight23) | Gemini-based code agent |
| **picoclaw** | mk-knight23 | [github.com/mk-knight23/picoclaw](https://github.com/mk-knight23) | Copilot-based Go code agent |

### Platform Docs

| Platform | Documentation |
|----------|---------------|
| Claude Code agents | [docs.anthropic.com/claude-code](https://docs.anthropic.com/claude/docs/claude-code) |
| Gemini AntiGravity | [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| Cursor rules | [docs.cursor.com/context/rules](https://docs.cursor.com/context/rules) |
| OpenCode agents | [opencode.ai](https://opencode.ai) |
| GitHub Copilot instructions | [docs.github.com/copilot/customizing-copilot](https://docs.github.com/en/copilot/customizing-copilot) |
| MCP (Model Context Protocol) | [modelcontextprotocol.io](https://modelcontextprotocol.io) |

---

## 🙏 CREDITS & CONTRIBUTIONS

### Primary Creator

**Musharraf Kazi** — [@mk-knight23](https://github.com/mk-knight23)
> AI Organization Architect · 6+ years AI engineering · Building self-evolving digital organizations
> Current projects: Open-Universe (60 apps), AI-VIBE Ecosystem, AI-SDK-Ecosystem, RALPH (134+ agents, 21 teams)

### Agency Agents — Original Author

**Mike Sitarzewski** — [@msitarzewski](https://github.com/msitarzewski)
> Creator of [agency-agents](https://github.com/msitarzewski/agency-agents) — the 68-agent personality system and the `convert.sh` script that generates 6 platform formats from a single source. All 68 core agents originate from his work. ⭐ Star his repo.

### Everything Claude Code — Original Author

**Daniel Isler** — [@disler](https://github.com/disler)
> Creator of [everything-claude-code](https://github.com/disler/everything-claude-code) — 48+ production-grade skills, coding standards, and agent configurations. ⭐ Star his repo.

### Platform Teams

| Team | Contribution |
|------|-------------|
| **Anthropic** | Claude Code agent system, MCP protocol specification |
| **Google DeepMind** | Gemini CLI + AntiGravity skill platform |
| **Cursor** | `.mdc` rule system for AI-native IDE |
| **OpenCode Labs** | OpenCode agent format and global agent directory |
| **GitHub** | Copilot custom instructions system |

---

## 📋 COLLECTION STATS

| Metric | Value |
|--------|-------|
| **Total Size (definitions)** | ~30 MB |
| **Total Size (with runtime, excluded)** | ~600 MB |
| **Total Files (committed)** | 2,700+ |
| **Total Directories** | 1,300+ |
| **Platforms Covered** | 11 |
| **Source Locations Scanned** | 15 |
| **Markdown Files** | 2,186 |
| **JSON Configs** | 168 |
| **TypeScript Files** | 122 |
| **YAML Manifests** | 80 |
| **Cursor Rules (.mdc)** | 68 |
| **Shell Scripts** | 11 |
| **Removed (runtime)** | ~499 files — conversation/session history |
| **Removed (duplicates)** | ~340 files — old lowercase paths + integration copies |
| **Secrets Redacted** | 6 files (MCP configs, platform configs) |

---

## 📄 LICENSE

**MIT** — All original work by [@mk-knight23](https://github.com/mk-knight23)

Individual agent definitions retain their original licenses:
- Agency agents — [MIT](https://github.com/msitarzewski/agency-agents/blob/main/LICENSE) · msitarzewski
- Everything-CC skills — [MIT](https://github.com/disler/everything-claude-code) · disler

---

<div align="center">

**Built with obsession. Deployed across 11 platforms. Runtime excluded. Definitions preserved.**

⭐ Star this repo · 🍴 Fork it · 📦 Use the agents

[@mk-knight23](https://github.com/mk-knight23) · [AGENTS-COLLECTION](https://github.com/mk-knight23/AGENTS-COLLECTION)

</div>

## Security

This project follows security best practices:
- No hardcoded credentials
- Dependency scanning enabled
- Security headers configured
- Regular security audits performed
