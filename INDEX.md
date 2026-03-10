# Agents Collection — Master Index

**Location:** `/Users/mkazi/Agents_Collection/`
**Generated:** 2026-03-10
**Total:** 3,475 files · 1,566 folders · 15 source locations · 4 parallel agents

---

## Directory Structure

```
Agents_Collection/
├── agents/          → Agent definitions by platform
├── skills/          → Skills / installable capabilities
├── prompts/         → Prompts, Pi prompts, Gemini agent files
├── workflows/       → Workflow definitions & implementation plans
├── mcp/             → MCP server configuration files
├── plugins/         → Plugin manifests, extensions
├── hooks/           → Pre/post execution hooks
├── commands/        → Slash commands
├── rules/           → Rules (Claude rules, Cursor .mdc rules)
├── docs/            → AGENTS.md, CLAUDE.md, project docs
├── configs/         → Platform config files
├── schemas/         → JSON schemas
├── data/            → Data files
└── assets/          → Asset files
```

---

## Agents (`agents/`) — 1,391 files

| Subfolder | Source | Format | Count |
|---|---|---|---|
| `claude-code/` | `~/.claude/agents/` | `.md` | 129 agents |
| `antigravity/` | `~/.gemini/antigravity/skills/` | `SKILL.md` per folder | 74 skills |
| `cursor/` | `~/.cursor/rules/` | `.mdc` | 68 rules |
| `opencode/` | `~/.config/opencode/agent/` | `.md` | 68 agents |
| `openclaw/` | `~/.openclaw/agents/` | `.md` + `.json` | 58 files |
| `nanoclaw/` | `NanoClaw/.nanoclaw/` | internal skill files | 41 files |
| `nanobot/` | `~/.nanobot/skills/agency-*/` | `skill.json` + `SKILL.md` | 68 folders |
| `zeroclaw/` | `zeroclaw/.gemini/agents/` | `.md` | 68 files |
| `picoclaw/` | `picoclaw/.github/copilot-instructions.md` | single `.md` | 1 file |
| `everything-cc/` | `everything-claude-code/agents/` | `.md` | 13 agents |
| `agency-source/` | `/tmp/agency-agents/` (source) | categorized `.md` | 85+ files |

---

## Skills (`skills/`) — 1,117 files

| Subfolder | Source | Count |
|---|---|---|
| `claude-code/` | `~/.claude/skills/` (SKILL.md + manifests) | 499 files |
| `nanoclaw/` | `NanoClaw/.claude/skills/` | 89 SKILL.md files |
| `openclaw/src/` | `~/.openclaw/skills/` | 27 files |
| `openclaw/project/` | `openclaw/skills/` (project-level) | 74 files |
| `nanobot/` | `~/.nanobot/skills/` | 69 folders |
| `everything-cc/` | `everything-claude-code/skills/` | 48 files |
| `everything-cc/opencode/` | `everything-claude-code/.opencode/` | 51 files |
| `github/` | `~/.github/skills/` | — |

---

## Prompts (`prompts/`) — 141 files

| Subfolder | Source | Format | Count |
|---|---|---|---|
| `openclaw-pi/` | `openclaw/.pi/prompts/` | frontmatter `.md` | 72 prompts |
| `zeroclaw-gemini/` | `zeroclaw/.gemini/` | Gemini Code Assist `.md` | 69 files |
| `openclaw-workflows/` | `openclaw/.agent/` | workflow `.md` | 1 file |

---

## Workflows (`workflows/`) — 9 files

| Subfolder | Source | Count |
|---|---|---|
| `claude-plans/` | `~/.claude/plans/` | 8 plans |
| `openclaw/` | `openclaw/.agent/workflows/` | 1 workflow |

---

## MCP (`mcp/`) — 4 files

| Subfolder | Source |
|---|---|
| `claude-code/` | `~/.claude/mcp.json` + `.mcp.json` |
| `nanoclaw/` | `NanoClaw/.mcp.json` |
| `cursor/` | `~/.cursor/mcp.json` |
| `openclaw/` | `openclaw/` MCP configs |

---

## Plugins (`plugins/`) — 509 files

| Subfolder | Source | Count |
|---|---|---|
| `claude-code/` | `~/.claude/plugins/` (manifests + `.md`) | 500 files |
| `openclaw/` | `~/.openclaw/extensions/` (manifests) | 9 files |
| `openclaw/pi-extensions/` | `openclaw/.pi/extensions/` | 4 files |
| `openclaw/extensions/` | `openclaw/extensions/` READMEs | — |

---

## Hooks (`hooks/`) — 8 files

| Subfolder | Source |
|---|---|
| `claude-code/` | `~/.claude/hooks/` |
| `openclaw/` | `~/.openclaw/hooks/` |

---

## Rules (`rules/`) — 19 files

| Subfolder | Source | Format |
|---|---|---|
| `claude-code/` | `~/.claude/rules/` | `.md` |
| `cursor/` | (same as `agents/cursor/`) | `.mdc` |

---

## Docs (`docs/`) — 31 files

| Subfolder | Contents |
|---|---|
| `nanoclaw/` | NanoClaw `docs/`, SKILL.md scans |
| `openclaw/` | `AGENTS.md`, `CLAUDE.md` |
| `zeroclaw/` | `AGENTS.md`, `CLAUDE.md` |
| `picoclaw/` | picoclaw `docs/` (19 files) |

---

## Configs (`configs/`) — 5 files

| Subfolder | Files |
|---|---|
| `claude-code/` | `GEMINI.md` |
| `openclaw/` | `openclaw.json` |
| `nanobot/` | `config.json` |
| `cursor/` | `mcp.json`, `cli-config.json` |
| `picoclaw/` | `config.json` |
| `zeroclaw/` | `config.toml`, `zeroclaw.json` |

---

## Source Locations Scanned

| # | Location | Type |
|---|---|---|
| 1 | `~/.claude/` | Claude Code (agents, skills, rules, plugins, plans, hooks, MCP) |
| 2 | `~/.gemini/antigravity/` | AntiGravity skills |
| 3 | `~/.cursor/rules/` | Cursor rules (.mdc) |
| 4 | `~/.config/opencode/agent/` | OpenCode global agents |
| 5 | `~/.openclaw/` | OpenClaw (agents, skills, hooks, extensions, config) |
| 6 | `~/.nanobot/skills/` | Nanobot skills |
| 7 | `~/.github/` | GitHub Copilot instructions + skills |
| 8 | `Open-Universe/NanoClaw/` | NanoClaw .claude/skills, .nanoclaw, docs, MCP |
| 9 | `Open-Universe/openclaw/` | openclaw .pi, .agent, skills, extensions, AGENTS.md |
| 10 | `Open-Universe/picoclaw/` | picoclaw .github, docs |
| 11 | `Open-Universe/zeroclaw/` | zeroclaw .gemini, AGENTS.md |
| 12 | `everything-claude-code/` | agents, skills, .opencode |
| 13 | `~/.claude/plans/` | Implementation plans |
| 14 | `/tmp/agency-agents/` | Agency source (68-agent repo + integrations) |
| 15 | VS Code / Cursor global | Configs, MCP |

---

## Quick Reference — Find by Type

| I need... | Look in |
|---|---|
| Claude Code agents | `agents/claude-code/` |
| AntiGravity skills | `agents/antigravity/` |
| Cursor rules | `agents/cursor/` |
| OpenCode agents | `agents/opencode/` |
| NanoClaw skills | `skills/nanoclaw/` or `agents/nanoclaw/` |
| Nanobot skills | `skills/nanobot/` |
| Pi prompts (openclaw) | `prompts/openclaw-pi/` |
| Gemini agents (zeroclaw) | `prompts/zeroclaw-gemini/` |
| Workflows | `workflows/` |
| MCP server configs | `mcp/` |
| Claude plugins | `plugins/claude-code/` |
| Hooks | `hooks/` |
| Platform configs | `configs/` |
| Project docs & AGENTS.md | `docs/` |
| Agency source (68 agents) | `agents/agency-source/` |
