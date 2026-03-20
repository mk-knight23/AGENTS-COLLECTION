# Awesome MCP Servers Collection

> Curated Model Context Protocol server configurations for AI coding agents.

---

## Core MCP Servers

### 1. Filesystem Server
Access and manipulate local files.

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/dir"],
      "env": {}
    }
  }
}
```

### 2. GitHub Server
Full GitHub API access for issues, PRs, repos.

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

### 3. Memory / Knowledge Graph
Persistent entity-relationship memory across sessions.

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "env": {
        "MEMORY_FILE_PATH": "~/.claude/memory/knowledge-graph.json"
      }
    }
  }
}
```

### 4. Sequential Thinking
Structured multi-step reasoning and problem decomposition.

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
      "env": {}
    }
  }
}
```

### 5. Puppeteer / Playwright Browser Automation
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-playwright"],
      "env": {}
    }
  }
}
```

---

## Database Servers

### 6. PostgreSQL
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://user:pass@localhost:5432/mydb"
      }
    }
  }
}
```

### 7. SQLite
```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite", "--db-path", "./data/app.db"],
      "env": {}
    }
  }
}
```

### 8. Redis
```json
{
  "mcpServers": {
    "redis": {
      "command": "npx",
      "args": ["-y", "mcp-server-redis"],
      "env": {
        "REDIS_URL": "redis://localhost:6379"
      }
    }
  }
}
```

---

## Web & Search Servers

### 9. Brave Search
```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "${BRAVE_API_KEY}"
      }
    }
  }
}
```

### 10. Firecrawl (Web Scraping)
```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "${FIRECRAWL_API_KEY}"
      }
    }
  }
}
```

### 11. Fetch / Web Reader
```json
{
  "mcpServers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"],
      "env": {}
    }
  }
}
```

---

## Cloud & Infrastructure Servers

### 12. AWS (Bedrock, S3, Lambda)
```json
{
  "mcpServers": {
    "aws": {
      "command": "npx",
      "args": ["-y", "mcp-server-aws"],
      "env": {
        "AWS_ACCESS_KEY_ID": "${AWS_ACCESS_KEY_ID}",
        "AWS_SECRET_ACCESS_KEY": "${AWS_SECRET_ACCESS_KEY}",
        "AWS_REGION": "us-east-1"
      }
    }
  }
}
```

### 13. Cloudflare
```json
{
  "mcpServers": {
    "cloudflare": {
      "command": "npx",
      "args": ["-y", "@cloudflare/mcp-server-cloudflare"],
      "env": {
        "CLOUDFLARE_API_TOKEN": "${CLOUDFLARE_API_TOKEN}",
        "CLOUDFLARE_ACCOUNT_ID": "${CLOUDFLARE_ACCOUNT_ID}"
      }
    }
  }
}
```

### 14. Kubernetes
```json
{
  "mcpServers": {
    "kubernetes": {
      "command": "npx",
      "args": ["-y", "mcp-server-kubernetes"],
      "env": {
        "KUBECONFIG": "~/.kube/config"
      }
    }
  }
}
```

### 15. Docker
```json
{
  "mcpServers": {
    "docker": {
      "command": "npx",
      "args": ["-y", "mcp-server-docker"],
      "env": {}
    }
  }
}
```

---

## Communication & Productivity Servers

### 16. Slack
```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}",
        "SLACK_TEAM_ID": "${SLACK_TEAM_ID}"
      }
    }
  }
}
```

### 17. Linear (Project Management)
```json
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": ["-y", "mcp-server-linear"],
      "env": {
        "LINEAR_API_KEY": "${LINEAR_API_KEY}"
      }
    }
  }
}
```

### 18. Notion
```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "mcp-server-notion"],
      "env": {
        "NOTION_TOKEN": "${NOTION_TOKEN}"
      }
    }
  }
}
```

---

## AI & Knowledge Servers

### 19. Qdrant (Vector Database)
```json
{
  "mcpServers": {
    "qdrant": {
      "command": "npx",
      "args": ["-y", "mcp-server-qdrant"],
      "env": {
        "QDRANT_URL": "http://localhost:6333",
        "QDRANT_API_KEY": "${QDRANT_API_KEY}"
      }
    }
  }
}
```

### 20. RAG Pipeline (Context7)
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"],
      "env": {}
    }
  }
}
```

### 21. Sentry (Error Tracking)
```json
{
  "mcpServers": {
    "sentry": {
      "command": "npx",
      "args": ["-y", "mcp-server-sentry"],
      "env": {
        "SENTRY_AUTH_TOKEN": "${SENTRY_AUTH_TOKEN}",
        "SENTRY_ORG": "${SENTRY_ORG}"
      }
    }
  }
}
```

---

## Observability & Monitoring Servers

### 22. Grafana
```json
{
  "mcpServers": {
    "grafana": {
      "command": "npx",
      "args": ["-y", "mcp-server-grafana"],
      "env": {
        "GRAFANA_URL": "http://localhost:3000",
        "GRAFANA_API_KEY": "${GRAFANA_API_KEY}"
      }
    }
  }
}
```

### 23. Prometheus
```json
{
  "mcpServers": {
    "prometheus": {
      "command": "npx",
      "args": ["-y", "mcp-server-prometheus"],
      "env": {
        "PROMETHEUS_URL": "http://localhost:9090"
      }
    }
  }
}
```

---

## Full Configuration Example

Complete `.claude/mcp.json` for a production setup:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."],
      "env": {}
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}" }
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "env": {}
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
      "env": {}
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-playwright"],
      "env": {}
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": { "BRAVE_API_KEY": "${BRAVE_API_KEY}" }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": { "POSTGRES_CONNECTION_STRING": "${DATABASE_URL}" }
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"],
      "env": {}
    }
  }
}
```

---

## Server Categories Quick Reference

| Category | Servers | Use Case |
|----------|---------|----------|
| **Core** | filesystem, memory, sequential-thinking | Basic file/memory/reasoning |
| **Code** | github, gitlab | Version control integration |
| **Browser** | playwright, puppeteer, firecrawl | Web automation & scraping |
| **Database** | postgres, sqlite, redis, qdrant | Data access |
| **Search** | brave-search, fetch | Web information retrieval |
| **Cloud** | aws, cloudflare, kubernetes, docker | Infrastructure management |
| **Comms** | slack, linear, notion | Collaboration tools |
| **Observability** | sentry, grafana, prometheus | Monitoring & debugging |
| **AI** | context7, qdrant | RAG & vector search |
