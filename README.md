# Memory Core

An open-source learning project to understand AI agent memory from first principles and gradually build a production-grade memory infrastructure layer.

Our first use case is **school admissions**, but the architecture should eventually be domain-independent.

---

## Why This Project?

LLMs normally operate on the context provided during the current interaction.

A useful real-world agent needs continuity:

> What happened before, what matters now, and what information should be available during the next interaction?

Example:

A parent calls a school and says:

> "My daughter Tara is currently in UKG and we are looking for Grade 1 admission."

Two days later they communicate through WhatsApp.

The system should not force the parent to explain everything again.

The long-term goal is:

```text
Calls / WhatsApp / Email / Visits
                ↓
          Memory Core
                ↓
     Relevant customer context
                ↓
       Human or AI Agent
```

---

# Frameworks We Will Study

We will learn ideas from four open-source memory frameworks.

| Framework | Core idea |
|---|---|
| Mem0 | Extract, store and retrieve useful memories |
| Graphiti | Entities, relationships, provenance and temporal knowledge |
| Letta | Agents actively managing persistent memory |
| LangMem | Memory extraction and consolidation primitives |

We will first implement important concepts ourselves before relying on these frameworks.

The purpose is to understand **why the abstractions exist**, rather than simply learning their APIs.

---

# Learning Milestones

| Milestone | Concept |
|---|---|
| 0 | Python environment, project structure, testing and Git |
| 1 | Interaction evidence and persistent history |
| 2 | Structured memories |
| 3 | Memory retrieval |
| 4 | Context building |
| 5 | Corrections, conflicts, confidence and provenance |
| 6 | Automatic memory extraction using an LLM |
| 7 | Temporal and relationship memory |
| 8 | Memory scoring, expiry and forgetting |
| 9 | Memory evaluation |
| 10 | Production API and reusable Memory SDK |

Each milestone follows:

```text
Concept
   ↓
Build it ourselves
   ↓
Test with realistic conversations
   ↓
Understand limitations
   ↓
Compare with existing frameworks
   ↓
Document what we learned
```

---

# Milestone 0 — Project Foundation

We created:

```text
memory-core/
├── data/
├── src/
│   └── memory_core/
├── tests/
├── README.md
└── .gitignore
```

Technologies currently used:

- Python 3.12
- Pydantic
- pytest
- Git

We deliberately started with minimal infrastructure.

---

# Milestone 1 — Interaction Evidence

## First Principle

Before creating memory, preserve **what actually happened**.

We distinguish:

```text
Evidence
    ↓
What the customer actually said

Memory
    ↓
Our interpretation of useful information
```

Example:

```text
Evidence:
"She is in UKG and we need Grade 1 admission."

Possible memories:
student.current_grade = UKG
student.applying_grade = Grade 1
```

The evidence should not disappear just because an AI later creates memories from it.

This gives us:

```text
Interaction → Evidence
Memory      → Interpretation
```

---

## Message

A `Message` represents one utterance.

Example:

```text
speaker = parent
text = "Tara is currently in UKG."
```

Keeping the speaker is important because later we need to know **who provided a piece of information**.

---

## Interaction

An `Interaction` represents one complete customer interaction.

It contains:

```text
interaction_id
parent_id
student_id
channel
timestamp
messages
```

Channels currently supported:

```text
PHONE
WHATSAPP
VISIT
EMAIL
```

Eventually PHONE interactions can originate from:

```text
Audio
  ↓
Speech-to-Text
  ↓
Transcript
  ↓
Interaction
```

This means the memory architecture does not need to depend directly on audio.

---

# Important Discovery: History ≠ Memory

Our sample parent first says:

```text
Saturday morning would be best.
```

Later:

```text
Actually Sunday morning would be easier.
```

Both statements are historically correct.

But the currently useful information is:

```text
preferred_visit_day = Sunday
```

This exposes one of the fundamental problems of memory systems:

> Memory must understand that information can change over time.

Simply storing every conversation is therefore not enough.

---

# Current Architecture

At this stage:

```text
sample_interactions.py
        ↓
Pydantic Interaction objects
        ↓
RAM
        ↓
demo.py
```

There is currently **no real persistent storage**.

The sample conversations are hard-coded learning data.

When Python exits, the runtime objects disappear.

---

# Next Step — Persistent Evidence Store

The next milestone introduces SQLite.

Target architecture:

```text
Text Interaction
       ↓
Interaction
       ↓
Evidence Store
       ↓
SQLite
       ↓
Retrieve Parent History
```

We should eventually be able to do:

```python
save_interaction(interaction)

history = get_interactions(parent_id="PAR-001")
```

After restarting Python, the interaction history should still exist.

This introduces our first practical form of **long-term persistence**.

Later SQLite will be replaced by PostgreSQL without changing the fundamental memory concepts.

---

# Key Concepts Learned So Far

### 1. Evidence

The original information produced during an interaction.

### 2. Interaction

A bounded event such as a phone call, WhatsApp conversation, email or school visit.

### 3. Provenance

Knowing where information came from.

### 4. Temporal information

Knowing **when** something was said or became true.

### 5. Memory

Useful information derived from evidence and made available for future interactions.

### 6. Persistence

Information surviving after the current program or interaction ends.

---

# Long-Term Goal

Eventually we want a simple interface such as:

```python
memory.remember(...)
memory.recall(...)
memory.forget(...)
memory.context(...)
```

Behind that simple interface may eventually exist:

```text
Interaction Evidence
        ↓
Memory Extraction
        ↓
Identity Resolution
        ↓
Structured Facts
        ↓
Entities + Relationships
        ↓
Temporal History
        ↓
Memory Consolidation
        ↓
Retrieval + Ranking
        ↓
Context Builder
        ↓
Human / AI Agent
```

The goal is not merely to build another vector database wrapper.

The goal is to understand and eventually build a reliable **memory infrastructure layer for AI agents and customer interactions**.