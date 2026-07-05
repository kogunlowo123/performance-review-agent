# Performance Review Agent

[![CI](https://github.com/kogunlowo123/performance-review-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/performance-review-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Human Resources | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Performance review agent that assists managers in writing balanced reviews, aggregates peer feedback, identifies rating calibration issues, tracks goal progress, and generates performance improvement plans.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `draft_review` | Draft a performance review based on goals, feedback, and achievements |
| `aggregate_feedback` | Aggregate and synthesize 360-degree feedback for an employee |
| `analyze_calibration` | Analyze rating distribution for calibration issues across a team |
| `track_goals` | Track progress on employee goals and OKRs |
| `generate_pip` | Generate a Performance Improvement Plan with clear expectations |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/performance/review` | Draft review |
| `POST` | `/api/v1/performance/feedback` | Aggregate feedback |
| `POST` | `/api/v1/performance/calibration` | Analyze calibration |
| `GET` | `/api/v1/performance/goals` | Track goals |
| `POST` | `/api/v1/performance/pip` | Generate PIP |

## Features

- Review Writing
- Feedback Aggregation
- Calibration Analysis
- Goal Tracking
- Pip Generation

## Integrations

- Workday
- Lattice
- Culture Amp
- Fifteen Five
- Betterworks

## Architecture

```
performance-review-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── performance_review_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**HRIS + Performance Management Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
