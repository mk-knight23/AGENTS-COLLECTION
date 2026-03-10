<div align="center">

# 🤖 Agents Collection

**The most comprehensive multi-platform AI agent library on a single machine.**

*3,475 files · 373 MB · 15 source locations · 11 platforms · 748 skills · 784 agent definitions*

[![Agents](https://img.shields.io/badge/Agents-784-blue?style=for-the-badge&logo=robot&logoColor=white)](./agents/)
[![Skills](https://img.shields.io/badge/Skills-748-green?style=for-the-badge&logo=puzzle&logoColor=white)](./skills/)
[![Prompts](https://img.shields.io/badge/Prompts-141-purple?style=for-the-badge&logo=chat&logoColor=white)](./prompts/)
[![Platforms](https://img.shields.io/badge/Platforms-11-orange?style=for-the-badge&logo=layers&logoColor=white)](./agents/)
[![Size](https://img.shields.io/badge/Size-373MB-red?style=for-the-badge&logo=database&logoColor=white)](./)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

---

*Collected from Claude Code · AntiGravity · Cursor · OpenCode · OpenClaw · NanoClaw · NanoBot · ZeroClaw · PicoClaw · GitHub Copilot · Everything-Claude-Code*

</div>

---

## Table of Contents

- [What Is This](#what-is-this)
- [Collection Size](#collection-size)
- [Quick Start](#quick-start)
- [Platform Coverage](#platform-coverage)
- [Agents](#agents-784-definitions)
- [Skills](#skills-748-installable-capabilities)
- [Prompts](#prompts-141-files)
- [Plugins & Extensions](#plugins--extensions-560-files)
- [Workflows](#workflows-9-files)
- [MCP Configs](#mcp-configs-4-files)
- [Hooks](#hooks-8-files)
- [Rules](#rules-19-files)
- [Configs](#configs-7-files)
- [Docs & Agent Protocols](#docs--agent-protocols-218-files)
- [Directory Structure](#directory-structure)
- [Source Locations](#source-locations-scanned)
- [Find Anything Fast](#find-anything-fast)

---

## What Is This

A single, organized collection of every AI agent, skill, prompt, workflow, plugin, hook, MCP config, and agent protocol scattered across a multi-platform AI engineering environment.

**Built from 15 source locations.** Scanned by 4 parallel AI agents. Organized into a structured library you can browse, reference, copy from, and build on.

**Who it's for:**
- AI engineers building multi-agent systems
- Developers integrating AI tools into existing workflows
- Researchers studying agent design patterns across platforms
- Anyone building with Claude Code, Cursor, OpenCode, or OpenClaw

---

## Collection Size

| Metric | Value |
|---|---|
| **Total disk size** | **373 MB** |
| **Total files** | **3,475** |
| **Total folders** | **1,566** |
| **Agent definitions** | **784** |
| **Skills** | **748** |
| **Prompts** | **141** |
| **Platforms covered** | **11** |
| **Source locations** | **15** |

### Size by Category

| Category | Size | Files |
|---|---|---|
| `agents/` | 355 MB | 1,391 |
| `skills/` | 9.4 MB | 1,117 |
| `plugins/` | 4.2 MB | 560 |
| `docs/` | 2.1 MB | 218 |
| `prompts/` | 1.6 MB | 141 |
| `workflows/` | 200 KB | 9 |
| `configs/` | 100 KB | 7 |
| `rules/` | 80 KB | 19 |
| `hooks/` | 60 KB | 8 |
| `mcp/` | 20 KB | 4 |

---

## Quick Start

```bash
# Browse agents by platform
ls agents/claude-code/        # 129 Claude Code agents
ls agents/antigravity/        # 74 AntiGravity skills
ls agents/cursor/             # 68 Cursor rules (.mdc)
ls agents/opencode/           # 68 OpenCode agents
ls agents/nanobot/            # 69 NanoBot skills
ls agents/agency-source/      # 68-agent source library

# Find a specific agent by name
grep -r "security" agents/ --include="*.md" -l

# Browse skills by platform
ls skills/claude-code/        # 499 Claude skills
ls skills/nanoclaw/           # 89 NanoClaw skills
ls skills/nanobot/            # 69 NanoBot skills
ls skills/everything-cc/      # 99 Everything-CC skills

# Find prompts
ls prompts/openclaw-pi/       # 72 Pi assistant prompts
ls prompts/zeroclaw-gemini/   # 69 Gemini Code Assist agents

# Check the master index
cat INDEX.md
```

---

## Platform Coverage

| Platform | Type | Format | Location | Count |
|---|---|---|---|---|
| **Claude Code** | AI coding assistant | `.md` agents | `agents/claude-code/` | 129 |
| **AntiGravity** | Gemini skill system | `SKILL.md` per folder | `agents/antigravity/` | 74 |
| **Cursor** | AI code editor | `.mdc` rules | `agents/cursor/` | 68 |
| **OpenCode** | AI coding platform | `.md` agents | `agents/opencode/` | 68 |
| **NanoBot** | WhatsApp AI bot | `skill.json` + `SKILL.md` | `skills/nanobot/` | 69 |
| **NanoClaw** | Multi-channel AI bot | `manifest.yaml` + `SKILL.md` | `skills/nanoclaw/` | 89 |
| **OpenClaw** | AI agent platform | `.md` + Pi prompts | `agents/openclaw/` + `prompts/openclaw-pi/` | 58 + 72 |
| **ZeroClaw** | Rust agent runtime | Gemini `.md` style | `prompts/zeroclaw-gemini/` | 69 |
| **PicoClaw** | Go agent runtime | Copilot instructions | `agents/picoclaw/` | 1 |
| **GitHub Copilot** | AI pair programmer | `copilot-instructions.md` | `agents/picoclaw/` | 68 embedded |
| **Everything-CC** | Claude Code toolkit | `.md` agents + skills | `agents/everything-cc/` | 13 + 99 |

---

## Agents — 784 Definitions

Agent definitions organized by platform. Each agent has a personality, mission, workflows, and deliverables.

### `agents/claude-code/` — 129 agents

Your full Claude Code agent roster including original agents plus The Agency's 68 specialists:

<details>
<summary>View all 129 agent categories</summary>

| Category | Examples |
|---|---|
| **Engineering** | `ai-engineer` · `backend-architect` · `frontend-developer` · `devops-automator` · `security-engineer` · `senior-developer` · `data-engineer` · `mobile-app-builder` |
| **Design** | `ui-designer` · `ux-researcher` · `ux-architect` · `brand-guardian` · `visual-storyteller` · `image-prompt-engineer` · `whimsy-injector` · `inclusive-visuals-specialist` |
| **Marketing** | `growth-hacker` · `tiktok-strategist` · `twitter-engager` · `instagram-curator` · `reddit-community-builder` · `content-creator` · `social-media-strategist` · `wechat-official-account` · `xiaohongshu-specialist` · `zhihu-strategist` |
| **Product** | `sprint-prioritizer` · `trend-researcher` · `feedback-synthesizer` · `behavioral-nudge-engine` |
| **Project Mgmt** | `studio-producer` · `studio-coach` · `experiment-tracker` · `project-shepherd` · `studio-operations` |
| **Testing** | `api-tester` · `performance-benchmarker` · `accessibility-auditor` · `tool-evaluator` · `reality-checker` · `evidence-collector` · `test-results-analyzer` · `workflow-optimizer` |
| **Support** | `support-responder` · `finance-tracker` · `infrastructure-maintainer` · `legal-compliance-checker` · `analytics-reporter` · `executive-summary-generator` |
| **Spatial** | `visionos-spatial-engineer` · `macos-spatial-metal-engineer` · `xr-interface-architect` · `xr-immersive-developer` · `xr-cockpit-interaction-specialist` · `terminal-integration-specialist` |
| **Specialized** | `agents-orchestrator` · `lsp-index-engineer` · `cultural-intelligence-strategist` · `developer-advocate` · `data-consolidation-agent` · `sales-data-extraction-agent` · `report-distribution-agent` |
| **Custom** | `analysis-agent` · `architecture-agent` · `ci-agent` · `codegen-agent` · `joker` · `rapid-prototyper` · `repo-scanner` · `project-shipper` |

</details>

### `agents/antigravity/` — 74 skill folders

Google AntiGravity skills for Gemini CLI. Each folder contains a `SKILL.md`.

```
~/.gemini/antigravity/skills/agency-ai-engineer/SKILL.md
~/.gemini/antigravity/skills/agency-backend-architect/SKILL.md
... (74 total)
```

### `agents/cursor/` — 68 `.mdc` rules

Cursor IDE global rules at `~/.cursor/rules/`. Auto-apply to matching file globs.

### `agents/opencode/` — 68 agents

Global OpenCode agents at `~/.config/opencode/agent/`. Reference with `@agent <name>` in chat.

### `agents/nanobot/` — 69 skills

NanoBot WhatsApp agent skills. Each with `skill.json` metadata + `SKILL.md`.

### `agents/agency-source/` — 68+ source files

The original [agency-agents](https://github.com/msitarzewski/agency-agents) source organized by division:

| Division | Agents |
|---|---|
| `engineering/` | ai-engineer · backend-architect · frontend-developer · devops-automator · security-engineer · senior-developer · data-engineer · mobile-app-builder · rapid-prototyper · technical-writer |
| `design/` | ui-designer · ux-architect · ux-researcher · brand-guardian · visual-storyteller · image-prompt-engineer · inclusive-visuals-specialist · whimsy-injector |
| `marketing/` | growth-hacker · content-creator · tiktok-strategist · twitter-engager · instagram-curator · reddit-community-builder · app-store-optimizer · social-media-strategist · wechat-official-account-manager · xiaohongshu-specialist · zhihu-strategist |
| `product/` | sprint-prioritizer · trend-researcher · feedback-synthesizer · behavioral-nudge-engine |
| `project-management/` | studio-producer · studio-operations · experiment-tracker · project-shepherd · senior-project-manager |
| `testing/` | api-tester · performance-benchmarker · accessibility-auditor · tool-evaluator · reality-checker · evidence-collector · test-results-analyzer · workflow-optimizer |
| `support/` | support-responder · finance-tracker · infrastructure-maintainer · legal-compliance-checker · analytics-reporter · executive-summary-generator |
| `spatial-computing/` | visionos-spatial-engineer · macos-spatial-metal-engineer · xr-interface-architect · xr-immersive-developer · xr-cockpit-interaction-specialist · terminal-integration-specialist |
| `specialized/` | agents-orchestrator · lsp-index-engineer · cultural-intelligence-strategist · developer-advocate · data-consolidation-agent · sales-data-extraction-agent · report-distribution-agent |

---

## Skills — 748 Installable Capabilities

Skills are modular, installable capabilities that extend AI agents with specific functionality.

### `skills/claude-code/` — 499 skills

Extracted from `~/.claude/skills/`. Includes `SKILL.md` and `manifest.yaml` files for every skill in the Claude Code ecosystem.

### `skills/nanoclaw/` — 89 skills

NanoClaw `.claude/skills/` including all Agency agents adapted to `manifest.yaml` format plus 20 original NanoClaw skills:

| Original NanoClaw Skills | Purpose |
|---|---|
| `add-whatsapp` | WhatsApp channel integration |
| `add-telegram` | Telegram channel integration |
| `add-discord` | Discord channel integration |
| `add-slack` | Slack channel integration |
| `add-gmail` | Gmail channel integration |
| `add-image-vision` | Multimodal image support |
| `add-voice-transcription` | Voice message transcription |
| `add-pdf-reader` | PDF reading in container |
| `add-ollama-tool` | Local LLM (Ollama) integration |
| `use-local-whisper` | On-device audio transcription |
| `convert-to-apple-container` | Apple Container migration |
| `x-integration` | X/Twitter automation |
| `add-telegram-swarm` | Multi-agent Telegram swarm |
| `add-parallel` | Parallel agent execution |
| `debug` · `customize` · `setup` | Core utility skills |
| `qodo-pr-resolver` · `get-qodo-rules` | PR automation |
| `update-nanoclaw` | Self-update |

### `skills/nanobot/` — 69 skills

NanoBot WhatsApp skill folders. Each contains `skill.json` + `SKILL.md`.

### `skills/everything-cc/` — 99 skills

Everything-Claude-Code toolkit skills + OpenCode-format skills.

### `skills/openclaw/` — 101 files

OpenClaw platform skills (global `~/.openclaw/skills/` + project-level).

---

## Prompts — 141 files

### `prompts/openclaw-pi/` — 72 prompts

OpenClaw Pi assistant prompts. Pi uses the `description:` frontmatter to auto-select the right agent:

```markdown
---
description: Expert AI/ML engineer specializing in machine learning...
---
# AI Engineer Agent
...
```

Key Pi prompts: `reviewpr.md` · `landpr.md` · `cl.md` · `is.md` + all 68 Agency agents

### `prompts/zeroclaw-gemini/` — 69 files

Gemini Code Assist agent files for ZeroClaw (Rust project). Loaded automatically by Gemini on PRs:

- `style-guide.md` — ZeroClaw Rust style guide
- `agents/` — all 68 Agency agents as Gemini context

---

## Plugins & Extensions — 560 files

### `plugins/claude-code/` — 500 files

Claude Code plugin manifests and documentation. Covers the full plugin marketplace including MCP server definitions, `plugin.json` metadata, and `SKILL.md` files.

### `plugins/openclaw/` — 60 files

OpenClaw extension manifests:
- `pi-extensions/` — 4 Pi UI extensions (`redraws.ts` · `diff.ts` · `prompt-url-widget.ts` · `files.ts`)
- Extension manifests for: msteams · matrix · zalo · zalouser · voice-call + more

---

## Workflows — 9 files

### `workflows/claude-plans/` — 8 plans

Claude Code implementation plans (`.md`). Multi-phase design and feature planning documents.

### `workflows/openclaw/` — 1 workflow

`update_clawdbot.md` — Full upstream sync protocol for OpenClaw forks: rebase strategy, Swift 6.2 fixes, macOS app rebuild, verification.

---

## MCP Configs — 4 files

Model Context Protocol server configurations:

| File | Platform | Servers Defined |
|---|---|---|
| `mcp/claude-code/mcp.json` | Claude Code global | All configured MCP servers |
| `mcp/nanoclaw/mcp.json` | NanoClaw project | NanoClaw-specific MCP |
| `mcp/cursor/mcp.json` | Cursor global | Cursor MCP servers |
| `mcp/openclaw/.mcp.json` | OpenClaw project | OpenClaw MCP |

---

## Hooks — 8 files

Pre/post execution hooks:

- `hooks/openclaw/` — OpenClaw hook scripts
- `hooks/claude-code/` — Claude Code session hooks (PostToolUse, PreToolUse, Stop events)

---

## Rules — 19 files

### `rules/claude-code/` — 19 rules

Global Claude Code rules loaded every session. Covers:
- `common/agents.md` — Agent orchestration protocol
- `common/coding-style.md` — Immutability, file organization, error handling
- `common/git-workflow.md` — Commit format, PR workflow, TDD approach
- `common/hooks.md` — Hook system patterns
- `common/patterns.md` — Repository pattern, API response format
- `common/performance.md` — Model selection strategy, context management
- `common/security.md` — Security checklist, secret management
- `common/testing.md` — Test coverage requirements, TDD workflow
- `python/` — Python-specific rules
- `typescript/` — TypeScript-specific rules

---

## Configs — 7 files

Platform configuration files:

| File | Platform | Size |
|---|---|---|
| `configs/openclaw/openclaw.json` | OpenClaw | 44 KB |
| `configs/nanobot/config.json` | NanoBot | — |
| `configs/cursor/mcp.json` | Cursor | — |
| `configs/cursor/cli-config.json` | Cursor | — |
| `configs/picoclaw/config.json` | PicoClaw | 12.5 KB |
| `configs/zeroclaw/config.toml` | ZeroClaw | 10.8 KB |
| `configs/claude-code/GEMINI.md` | Gemini global | — |

---

## Docs & Agent Protocols — 218 files

### AGENTS.md files

Agent engineering protocols from each project:

| Project | Protocol Focus |
|---|---|
| `docs/zeroclaw/AGENTS.md` | Rust-first agent runtime, trait-driven architecture, KISS principles |
| `docs/openclaw/AGENTS.md` | OpenClaw project guidelines, module organization, security trust model |
| `docs/openclaw/CLAUDE.md` | Coding style, release channels, testing guidelines |

### Project Docs

- `docs/nanoclaw/` — NanoClaw architecture and integration docs (8 files)
- `docs/picoclaw/` — PicoClaw Go project documentation (19 files)
- `docs/` root — SKILL.md files scanned from all Open-Universe projects (218 total)

---

## Directory Structure

```
Agents_Collection/                    ← 373 MB total
│
├── README.md                         ← This file
├── INDEX.md                          ← Master quick-reference index
│
├── agents/                           ← 1,391 files (355 MB)
│   ├── agency-source/                ← 68-agent source library (by division)
│   │   ├── design/                   ← 8 agents
│   │   ├── engineering/              ← 10 agents
│   │   ├── marketing/                ← 11 agents
│   │   ├── product/                  ← 4 agents
│   │   ├── project-management/       ← 5 agents
│   │   ├── spatial-computing/        ← 6 agents
│   │   ├── specialized/              ← 7 agents
│   │   ├── strategy/                 ← agents
│   │   ├── support/                  ← 6 agents
│   │   ├── testing/                  ← 8 agents
│   │   └── integrations/             ← Claude/Cursor/OpenCode/Cursor/Windsurf/Aider formats
│   ├── antigravity/                  ← 74 AntiGravity SKILL.md folders
│   ├── claude-code/                  ← 129 Claude Code .md agents
│   ├── cursor/                       ← 68 Cursor .mdc rules
│   ├── everything-cc/                ← 13 Everything-CC agents
│   ├── nanobot/                      ← 69 NanoBot skill folders
│   ├── nanoclaw/                     ← 41 NanoClaw internal files
│   ├── openclaw/                     ← 58 OpenClaw agent .md + .json
│   ├── opencode/                     ← 68 OpenCode .md agents
│   ├── picoclaw/                     ← copilot-instructions.md (68 embedded)
│   └── zeroclaw/                     ← 68 Gemini Code Assist .md agents
│
├── skills/                           ← 1,117 files (9.4 MB)
│   ├── claude-code/                  ← 499 skill manifests from ~/.claude/skills/
│   ├── everything-cc/                ← 99 Everything-CC + OpenCode skills
│   ├── github/                       ← GitHub Copilot skills
│   ├── nanobot/                      ← 69 NanoBot skill folders
│   ├── nanoclaw/                     ← 89 NanoClaw skills (manifest.yaml + SKILL.md)
│   └── openclaw/                     ← 101 OpenClaw platform skills
│       ├── src/                      ← ~/.openclaw/skills/
│       └── project/                  ← openclaw/skills/ project-level
│
├── prompts/                          ← 141 files (1.6 MB)
│   ├── openclaw-pi/                  ← 72 Pi assistant prompts
│   ├── openclaw-workflows/           ← 1 workflow
│   └── zeroclaw-gemini/              ← 69 Gemini Code Assist files
│
├── plugins/                          ← 560 files (4.2 MB)
│   ├── claude-code/                  ← 500 plugin manifests
│   └── openclaw/                     ← 60 extension manifests + Pi extensions
│
├── workflows/                        ← 9 files (200 KB)
│   ├── claude-plans/                 ← 8 implementation plans
│   └── openclaw/                     ← 1 upstream sync workflow
│
├── mcp/                              ← 4 files (20 KB)
│   ├── claude-code/
│   ├── cursor/
│   ├── nanoclaw/
│   └── openclaw/
│
├── hooks/                            ← 8 files (60 KB)
│   ├── claude-code/
│   └── openclaw/
│
├── rules/                            ← 19 files (80 KB)
│   ├── claude-code/                  ← 19 session rules
│   └── cursor/                       ← (same as agents/cursor/)
│
├── docs/                             ← 218 files (2.1 MB)
│   ├── nanoclaw/
│   ├── openclaw/
│   ├── picoclaw/
│   └── zeroclaw/
│
├── configs/                          ← 7 files (100 KB)
│   ├── claude-code/
│   ├── cursor/
│   ├── nanobot/
│   ├── openclaw/
│   ├── picoclaw/
│   └── zeroclaw/
│
├── commands/                         ← (empty — none found on system)
├── schemas/                          ← (empty — none found on system)
├── data/                             ← (empty — none found on system)
└── assets/                           ← (empty — none found on system)
```

---

## Source Locations Scanned

| # | Source Path | What Was Collected |
|---|---|---|
| 1 | `~/.claude/agents/` | 129 Claude Code agents |
| 2 | `~/.claude/skills/` | 499 skill manifests |
| 3 | `~/.claude/rules/` | 19 session rules |
| 4 | `~/.claude/plugins/` | 500 plugin manifests |
| 5 | `~/.claude/plans/` | 8 implementation plans |
| 6 | `~/.gemini/antigravity/` | 74 AntiGravity skill folders |
| 7 | `~/.cursor/rules/` | 68 Cursor .mdc rules |
| 8 | `~/.config/opencode/agent/` | 68 OpenCode agents |
| 9 | `~/.openclaw/` | 58 agents · 27 skills · hooks · extensions · config |
| 10 | `~/.nanobot/skills/` | 69 NanoBot skill folders |
| 11 | `Open-Universe/NanoClaw/` | 89 skills · 41 internal · docs · MCP |
| 12 | `Open-Universe/openclaw/` | 72 prompts · 74 skills · 4 Pi extensions · AGENTS.md |
| 13 | `Open-Universe/picoclaw/` | copilot-instructions · 19 docs |
| 14 | `Open-Universe/zeroclaw/` | 69 Gemini agents · AGENTS.md |
| 15 | `everything-claude-code/` | 13 agents · 99 skills |

**+ Agency source** (`/tmp/agency-agents/`) — 68-agent library with integrations for 6 platforms

---

## Find Anything Fast

```bash
# By platform
ls agents/claude-code/                     # Claude Code
ls agents/antigravity/                     # AntiGravity / Gemini
ls agents/cursor/                          # Cursor
ls agents/opencode/                        # OpenCode
ls agents/nanobot/                         # NanoBot
ls skills/nanoclaw/                        # NanoClaw

# By type
ls workflows/                              # Workflows
ls prompts/openclaw-pi/                    # Pi prompts
ls prompts/zeroclaw-gemini/                # Gemini agents
ls mcp/                                    # MCP configs
ls hooks/                                  # Hooks
ls rules/claude-code/                      # Session rules
ls plugins/claude-code/                    # Plugin manifests

# Search by keyword
grep -r "security" agents/ -l             # All security agents
grep -r "marketing" agents/ -l            # All marketing agents
grep -r "react" skills/ -l               # Skills mentioning React
grep -r "database" skills/ -l            # Database-related skills

# Find by agent name
find agents/ -name "*backend*"
find agents/ -name "*orchestrat*"
find skills/ -name "*whisper*"

# Count
find agents/ -name "*.md" | wc -l        # Total agent files
find skills/ -name "SKILL.md" | wc -l    # Total installable skills
```

---

## The 68 Core Agency Agents

These 68 agents are installed in every platform (Claude Code, Cursor, OpenCode, NanoBot, NanoClaw, OpenClaw Pi, ZeroClaw Gemini, GitHub Copilot):

| Division | Agents |
|---|---|
| **Engineering (10)** | ai-engineer · backend-architect · frontend-developer · devops-automator · security-engineer · senior-developer · data-engineer · mobile-app-builder · rapid-prototyper · technical-writer |
| **Design (8)** | ui-designer · ux-architect · ux-researcher · brand-guardian · visual-storyteller · image-prompt-engineer · inclusive-visuals-specialist · whimsy-injector |
| **Marketing (11)** | growth-hacker · content-creator · tiktok-strategist · twitter-engager · instagram-curator · reddit-community-builder · app-store-optimizer · social-media-strategist · wechat-official-account-manager · xiaohongshu-specialist · zhihu-strategist |
| **Product (4)** | sprint-prioritizer · trend-researcher · feedback-synthesizer · behavioral-nudge-engine |
| **Project Mgmt (5)** | studio-producer · studio-operations · experiment-tracker · project-shepherd · senior-project-manager |
| **Testing (8)** | api-tester · performance-benchmarker · accessibility-auditor · tool-evaluator · reality-checker · evidence-collector · test-results-analyzer · workflow-optimizer |
| **Support (6)** | support-responder · finance-tracker · infrastructure-maintainer · legal-compliance-checker · analytics-reporter · executive-summary-generator |
| **Spatial (6)** | visionos-spatial-engineer · macos-spatial-metal-engineer · xr-interface-architect · xr-immersive-developer · xr-cockpit-interaction-specialist · terminal-integration-specialist |
| **Specialized (7)** | agents-orchestrator · lsp-index-engineer · cultural-intelligence-strategist · developer-advocate · data-consolidation-agent · sales-data-extraction-agent · report-distribution-agent |
| **Strategy (3)** | agentic-identity-trust-architect · autonomous-optimization-architect · reality-checker |

---

## Credits

- **[The Agency](https://github.com/msitarzewski/agency-agents)** — 68 personality-driven specialist agents (MIT License)
- **[Everything Claude Code](https://github.com/everything-claude-code/everything-claude-code)** — Agents, skills, and coding standards toolkit
- **[NanoClaw](https://github.com/NanoClaw/nanoclaw)** — Multi-channel AI bot skills engine
- **[OpenClaw](https://github.com/openclaw/openclaw)** — Open-source AI agent platform
- **[ZeroClaw](https://github.com/zeroclaw/zeroclaw)** — Rust-first autonomous agent runtime
- **Musharraf Kazi** — Collection, organization, cross-platform installation

---

<div align="center">

**373 MB · 3,475 files · 11 platforms · One collection.**

*MIT License — Use freely, build boldly.*

</div>
