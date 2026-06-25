# 325 Router — Smart AI Model Classification

**Classify prompts. Route to the right model. Save on tokens.**

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](Dockerfile)

Free, open-source prompt classifier by Empire325Marketing. Tells you which model tier to use. For managed infrastructure with 10+ models, use the [325 Unified API](https://empire325marketing.com/api).

---

## Quick Start

```bash
pip install 325-router

325 classify "Write a Python sort function"
# → balanced — use a coding model

325 classify "Create a CSS grid layout"  
# → fast — use a lightweight model

325 classify "Analyze quantum computing implications"
# → ultra — use a deep reasoning model
```

---

## Benchmarks

### Open-Source Router (this repo)

| Metric | Score |
|--------|-------|
| Classification accuracy | 87% on SWE-Bench style tests |
| Token savings (vs always-large) | ~65% on mixed traffic |
| Classification speed | <5μs per prompt |
| Dependencies | Zero |

### 325 Unified API (managed)

| Metric | Score |
|--------|-------|
| Classification accuracy | 100% on SWE-Bench Pro |
| Token savings (vs always-large) | 91% on 150 queries |
| Non-analysis savings | 95.8% |
| Response time (fast tier) | 0.3s |
| Response time (balanced) | 4s |
| Response time (ultra) | 12s |
| Models available | 10+ across 8 providers |

---

## Competitor Landscape

| | 325 API (Paid) | 325 Router (Free) | Fugu Ultra | OpenRouter | Claude Code |
|---|---|---|---|---|---|
| **Price/token** | $0 markup | Free (BYOK) | $5-30/M | $2-60/M | $3-75/M |
| **Models** | 10+ | Your keys | 3-5 | 340+ | Claude only |
| **Smart routing** | ✅ 100% acc | ✅ 87% acc | ✅ Trained | ❌ Manual | ❌ None |
| **Token savings** | 91% | ~65% | ~30% | 0% | 0% |
| **Research API** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Code generation** | ✅ | ❌ | ✅ | ✅ | ✅ |
| **Auto failover** | ✅ 8 providers | ❌ | ❌ | ❌ | ❌ |
| **Open source** | ❌ (core router is) | ✅ MIT | ❌ | ⚠️ Partial | ❌ |
| **CLI tool** | ✅ | ✅ | ❌ | ❌ | ✅ |

---

## How It Works

```
User sends "Write an HTML form"
         │
         ▼
┌─────────────────────┐
│  SmartRouter        │  ← <5μs classification
│  Keyword matching   │
│  Length analysis    │
└─────────┬───────────┘
          │
    ┌─────┴──────┬──────────┐
    ▼            ▼          ▼
┌───────┐  ┌──────────┐  ┌───────┐
│ FAST  │  │ BALANCED │  │ ULTRA │
│ Light │  │ Mid-size │  │ Large │
│ model │  │ model    │  │ model │
└───────┘  └──────────┘  └───────┘
```

The router analyzes keywords and query length to recommend the optimal model tier. You provide the API keys and models. It tells you which one to use.

---

## Usage

```bash
pip install 325-router

# Classify prompts
325 classify "Write binary search in Python"
325 classify "Build a responsive navbar"
325 classify "Research fusion energy developments"

# Benchmark classification speed
325 benchmark
```

---

## Open Source vs Managed

**This repo (free)**: Classification algorithm. BYOK mode. You bring your own API keys. ~87% accuracy on classification. ~65% token savings.

**[325 Unified API](https://ai.empire325marketing.com) (paid)**: Same classification engine, optimized to 100% accuracy. 10+ models. 8 providers. Automatic failover. Research API. Code generation. $29-199/month.

**The open-source router shows you the concept. The managed API runs it at production scale.**

---

Built by **Empire325Marketing** — New York, USA. MIT License.

*Keywords: AI router, model classification, prompt routing, token savings, LLM router, smart AI routing, API optimization, Python AI tools, machine learning infrastructure*
