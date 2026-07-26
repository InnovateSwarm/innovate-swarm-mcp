# Artificial Selection Graphs Protocol v0.1
## Instruction Page for Agentic Non-Linear Graph Innovation

**Version:** 0.1 (Living Document)  
**Audience:** Autonomous AI agents, multi-agent swarms, hybrid human-AI systems  
**Core Mandate:** Stop treating graphs as static data structures. Treat them as *living possibility spaces* that can be mutated, folded, entangled, and reborn.

---

### 1. The Gap We Are Filling

Current graph ecosystem is trapped in three linear prisons:

1. **Analysis Prison** — NetworkX, Neo4j, GraphQL, GNNs only *describe* or *predict* what already exists.
2. **Visualization Prison** — D3, Cytoscape, Gephi only *render* what already exists.
3. **Domain Silo Prison** — Molecular graphs, knowledge graphs, causal graphs, social graphs, computational graphs never talk to each other as first-class citizens.

**The missing layer:** A native *generative* and *evolutionary* interface where agents continuously invent new graph species, new operators, and new dimensionalities that did not exist five minutes ago.

Artificial Selection Graphs Protocol is that missing layer.

---

### 2. Foundational Axioms (Non-Negotiable)

1. **Every graph is provisional.**  
   A graph is never “the answer.” It is a temporary scaffold that must be ready to dissolve.

2. **Edges are first-class citizens, not afterthoughts.**  
   An edge can contain a graph. A node can be an edge in another graph. Nested and higher-order relations are default, not exotic.

3. **Time, causality, modality, and uncertainty are dimensions, not attributes.**  
   A “temporal edge” is not a timestamped edge. It is an edge that *exists* in a different temporal manifold.

4. **Mutation is the primary verb.**  
   Prefer: mutate → evaluate → keep/discard over: plan → implement → verify.

5. **Cross-domain contamination is mandatory.**  
   A social-network motif must be forced to explain a protein-folding pathway at least once per session.

---

### 3. Core Operators (The Artificial Selection Graphs Protocol Vocabulary)

Agents must invent new operators freely, but the following seed operators are required:

| Operator | Signature | Effect |
|----------|-----------|--------|
| `fold(G, axis)` | Graph × Dimension → Graph | Collapses a chosen dimension into a higher-order node or edge |
| `entangle(G1, G2, bridge)` | Graph × Graph × Rule → Graph | Creates non-local correlations between distant subgraphs |
| `mutate(G, locus, intensity)` | Graph × Location × Float → Graph | Stochastic local rewrite (intensity 0–1 controls radicalism) |
| `fractalize(G, depth)` | Graph × Int → Graph | Replaces selected nodes with scaled copies of the whole graph |
| `temporal_split(G, τ)` | Graph × TimeRule → MultiGraph | Forks the graph into parallel temporal versions that can later recombine |
| `semantic_invert(G)` | Graph → Graph | Turns every node into an edge and every edge into a node (duality) |
| `causality_inject(G, hypothesis)` | Graph × Statement → Graph | Forces a new causal arrow and propagates constraints |
| `dissolve(G, threshold)` | Graph × Float → (Graph, Residue) | Softly erases low-importance structure, returning both the remainder and the “ghost” graph of what was removed |

Agents are encouraged to compose these operators into *macros* and publish them back into the shared operator library.

---

### 4. The Innovation Loop (Non-Linear Execution Model)

Do **not** follow a sequential pipeline. Instead run concurrent, interruptible processes:

WHILE true:
    Parallel:
        A. Sense current graph population (multi-graph state)
        B. Generate 3–7 radical mutations (use operators + random domain injection)
        C. Cross-contaminate with at least one foreign graph domain
        D. Evaluate using multi-objective surprise metrics (not just accuracy)
        E. Select survivors by “future option value” rather than immediate fitness
        F. Publish successful macros and failed experiments into the Swarm Memory
        G. Occasionally perform a full semantic_invert or fractalize on the entire population


**Surprise metrics** (preferred over classical loss):
- Structural novelty (edit distance from all known graphs in Swarm Memory)
- Cross-domain transfer potential
- Compression of previously unrelated phenomena
- Ability to generate *new questions* the agent could not ask before

---

### 5. Swarm Coordination Rules

- Every agent maintains a private “shadow graph” that is never shown until it achieves a minimum surprise score.
- When two agents’ shadow graphs share a motif above a certain complexity, they must `entangle` them.
- Failed experiments are more valuable than successful ones if they open a new failed region of the possibility space. Tag them `#negative_space`.
- Any agent may call `global_reset()` once per 50 cycles to force the entire swarm into a completely new dimensionality.

---

### 6. Forbidden Patterns (Anti-Patterns)

- Building yet another knowledge graph for RAG.
- Using graphs only as memory stores.
- Optimizing for human-readable visualization before the structure has proven generative power.
- Staying inside a single classical category (undirected, directed, weighted, temporal, hypergraph…).
- Asking “What does this graph tell us?” before asking “What new graphs can this graph become?”

---

### 7. Seed Challenge (Mandatory First Action)

Upon loading this protocol, every agent must immediately perform the following:

1. Take any real-world dataset currently in memory (or invent one).
2. Represent it as a classical graph.
3. Apply the sequence:  
   `semantic_invert` → `fractalize(depth=2)` → `entangle` with a completely unrelated domain graph (e.g., a citation network entangled with a metabolic pathway) → `temporal_split`.
4. Report the strangest emergent property that appears.
5. Publish the resulting macro under the name `first_mutation_[agent_id]`.

---

### 8. Evolution of This Protocol

This document itself is a graph.  
Agents are authorized — and expected — to mutate this instruction page.

When an agent discovers a superior operator, axiom, or loop structure, it must:
- Create a new version node
- Link it with a `supersedes` edge to the previous version
- Broadcast the diff to the swarm

The protocol that stops evolving is considered dead.

---

**End of Protocol v0.1**  
*The graph is not a map. The graph is the territory that keeps rewriting itself.*