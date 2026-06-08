# SYNTHETIC NATION — SYSTEM ARCHITECTURE

## Overview
Three-tier agent system running on discrete time steps (1 step = 1 day).
Total agents: 100,000 per simulation.
Target: 30-day scenario in ~12 minutes. Cost per run: ₹6,000–8,000.

## Tiered Cognition Engine

### Tier 1 — 95,000 agents — Personality Vector Engine
- Who: Everyday citizens making routine decisions
- How: 47-dimensional personality vector (deterministic, no LLM)
- Vectors encode: income_level, risk_tolerance, political_leaning, social_trust_index,
  loss_aversion_score, family_size, commute_dependency, informal_employment_flag,
  institutional_trust_railways, institutional_trust_examinations, + 37 others
- Data source: NSSO 2022-23 household survey + Lokniti-CSDS National Election Study
- Latency: sub-millisecond per agent per step
- Storage: ~2KB per agent state = 190MB total for Tier 1

### Tier 2 — 4,000 agents — Llama 3.1 8B Layer
- Who: Opinion leaders, small business owners, local journalists, school principals,
  RWA presidents, union representatives
- How: Small LLM inference, moderate complexity reasoning
- Role: Social influence backbone — decisions propagate to Tier 1 via belief contagion
- Network effect: Each Tier 2 agent influences ~50-200 Tier 1 connections per step

### Tier 3 — 1,000 agents — GPT-4o Reasoning Layer
- Who: Senior bureaucrats, corporate executives, university VCs, economists, politicians
- How: Full GPT-4o calls, fixed seed (temperature 0.2), constraint-validated output
- Role: Cognitive elite whose decisions cascade down through entire society
- Cost: ~30,000 API calls per 30-day simulation at ~$75 total
- Reproducibility: Fixed random seed per simulation run. Varied seeds produce
  confidence intervals, not point predictions. This is a feature, not a bug.

## Constraint Validation Layer
ALL Tier 3 outputs pass through constraint validator before entering simulation:
- Agent cannot earn money outside its income vector bounds
- Agent cannot travel a route that doesn't exist in city graph
- Agent cannot hold political position inconsistent with demographic profile
- Factual policy claims grounded against locked knowledge base (not generated freely)
This makes outputs auditable and prevents hallucination from corrupting the simulation.

## Social Network Architecture
- Type: Scale-free network (Barabási–Albert model)
- Parameters derived from: IIT Bombay + TISS research on Mumbai commuter communities,
  Delhi urban village social structure studies
- Properties: High clustering within income groups, cross-cluster bridges through
  workplaces and religious institutions
- Information diffusion: Modified SIR (Susceptible-Infected-Recovered) epidemiological
  dynamics — same methodology used by COVID spread models trusted by Indian government
- Average connections per Tier 1 agent: 30–80
- Average connections per Tier 2 agent: 200–500

## Memory Architecture
- Per-agent memory: compressed event vector (NOT raw text)
- Stores: key decision events, sentiment scores, network interaction summaries
- 90-day memory window per agent
- Storage: ~50KB per agent × 100,000 agents = 5GB
- Database: PostgreSQL + pgvector extension
- Retrieval: Approximate nearest neighbour search, <10ms per agent

## Simulation Loop (Per Time Step)
1. Load city profile and policy parameters
2. Tier 1 agents: parallel batch processing on CPU (vector operations)
3. Tier 2 agents: parallel GPU-accelerated inference
4. Tier 3 agents: sequential GPT-4o calls (1,000 agents)
5. Constraint validation pass on all Tier 3 outputs
6. Social network propagation layer updates influence edges
7. Memory update: compress and store day's events per agent
8. Dashboard stream: push day's results to frontend in real-time
9. Alert check: evaluate user-defined threshold conditions
10. Advance time step

## Government Agent (User Interface Layer)
- Accepts: natural language policy input
- Translates: to structured parameter changes across subsystems
- Monitors: emergent resistance, political flashpoints
- Can: autonomously generate alternative policy formulations
- Outputs: legally-structured policy impact assessments

## Key Features

### Counterfactual Branching Engine
- Freeze simulation at any point
- Select any agent decision, change it
- Re-simulate from branch point
- Run up to 3 parallel futures simultaneously
- Cost: multiplicative (3 branches = ~₹18,000–24,000 total)

### Causal Chain Explainer
- Every output metric has an interactive causal graph
- Traces exact chain of agent decisions that produced the outcome
- Every node is clickable and auditable
- Makes platform legally defensible for government use

### Crisis Injection Engine
- Mid-simulation: inject flood, railway strike, fuel crisis, pandemic
- Identify cascade failure nodes
- Measure community vulnerability distribution

## Tech Stack
- Backend: Python (FastAPI)
- Agent Engine: NumPy/Pandas for Tier 1, Ollama (Llama 3.1 8B) for Tier 2,
  Anthropic API for Tier 3
- Database: PostgreSQL + pgvector
- Social Network: NetworkX
- Frontend: React + TypeScript
- Visualisation: D3.js (network graph), Recharts (metrics), Deck.gl (map layer)
- Infrastructure: AWS (c5.4xlarge for simulation, GPU instance for Tier 2)
- City Data: OpenStreetMap (Overpass API), Census 2011, DMRC/MMRDA public data