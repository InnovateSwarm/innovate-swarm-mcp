# Content ------------------------------------------------------------------------------------------------------------------------------------------------

## Agent Brain Core
**The Open Executable Memory Layer for AI Agents**

The foundational open-source infrastructure for reliable, production-grade AI agents. Turns messy company data into versioned, executable **skills** that agents can load and run autonomously.

This is the open core of the **Request for Agent Brains (RFA-Brain)** vision.

### Why Agent Brain Exists

Current agents forget everything, require constant prompting, and can't reliably use real company knowledge.  
Agent Brain solves this by acting as **Git + Neural Compiler + Living Knowledge Graph** for organizations.

### Core Features (Open Source)

- **Universal Ingestion**: Slack, Email, Notion, Google Drive, Jira, PDFs, Markdown, code repos
- **Multimodal Support**: Extract processes from videos, images, and screen recordings (via external model APIs)
- **Executable Skill Files**: Outputs versioned, structured skills agents can directly `load()`
- **Temporal Knowledge Graph**: Tracks changes over time with full provenance
- **Versioning & Rollback**: Every knowledge update is versioned like Git
- **Open Skill Schema**: Standardized JSON + decision-tree format (see `schema/`)
- **Proactive Hooks**: Webhooks and real-time update streams
- **Audit & Provenance**: Every fact links back to source + timestamp + owner
- **Self-hosted**: Runs locally or in your VPC

### Quick Start

1. Installation

```bash
pip install agent-brain-core
````


# Basic Usage ------------------------------------------------------------------------------------------------------------------------------------------------

from agent_brain import Brain

## Initialize
brain = Brain(
    storage_path="./company_brain",
    embedding_model="text-embedding-3-small"
)

## Ingest data
brain.ingest_directory("./company_docs/")
brain.ingest_slack_export("slack_export.zip")
brain.ingest_emails("mailbox.mbox")

## Generate executable skills
skills = brain.generate_skills(
    domain="customer_support",
    version="3.2"
)

## Save and version
brain.save_version("v2026-04-28")
print(skills["refund_playbook"].to_json())



# Loading skils into your agent ------------------------------------------------------------------------------------------------------------------------------------------------

from agent_brain import load_skill

skill = load_skill("company_brain/skills/refund_playbook_v3.2.json")

## Your agent can now execute it directly
result = skill.execute(context=current_ticket)



# Project Structure  ------------------------------------------------------------------------------------------------------------------------------------------------

agent-brain/
├── core/                  # Main engine
├── schema/                # Open Skill File schema (v1)
├── connectors/            # Slack, Gmail, Notion, etc.
├── examples/              # Vertical examples (finance, support, manufacturing)
├── tests/                 # Evaluation harness
└── docs/


# Open Skill File Schema  ------------------------------------------------------------------------------------------------------------------------------------------------

Located in /schema/agent_skill_v1.jsonKey
## properties:
name, version, domain
steps (with decision trees)
tools (pre-wired API calls)
provenance
confidence_score
required_context

# Roadmap  ------------------------------------------------------------------------------------------------------------------------------------------------

Advanced multimodal extraction (video → playbook)
Real-time observation engine
Swarm coordination primitives
Enterprise compliance pack (SOC2, HIPAA)
Managed Brain Cloud (premium)

# Commercial Offering  ------------------------------------------------------------------------------------------------------------------------------------------------

This repository contains only the open core.
For managed hosting, advanced connectors, compliance, SLAs, and vertical brains (Finance Brain, Manufacturing Brain, etc.), check out Agent Brain Cloud (coming Q3 2026).

# Contributing  ------------------------------------------------------------------------------------------------------------------------------------------------

## We welcome contributions!
See CONTRIBUTING.md and join the discussion in Discussions.
Biggest needs right now:
More connectors
Evaluation benchmarks
Vertical skill templates

# License  ------------------------------------------------------------------------------------------------------------------------------------------------

Apache License 2.0 — fully open for commercial use.


# Community & Links  ------------------------------------------------------------------------------------------------------------------------------------------------

Twitter/X: @agentbrain
Discord: (link in repo)
Original RFA-Brain: View the full manifesto

Built for the Agent Economy.

Let's make every company AI-native.



