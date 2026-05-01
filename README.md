# Local LLM Agent System (TinyLlama, Tools, No APIs)

## 🔥 What this is

A minimal **agent system that runs entirely locally** using a small language model (TinyLlama), with real tool usage.

> No OpenAI API
> No external dependencies
> No hidden cloud calls

---

## 🎯 Why this exists

Most “AI agent” demos rely on:

* large proprietary models
* API calls
* high latency and cost

This project answers a harder question:

> **Can a small local model behave like an agent and actually use tools?**

---

## 🧠 What this demonstrates

* Tool-using agents **do not require large models**
* Simple reasoning loops can be implemented with minimal infrastructure
* Practical LLM systems can run **fully offline**

---

## ⚙️ System Overview

```
User Query
   ↓
TinyLlama (reasoning + tool selection)
   ↓
Tool Execution (calculator / file / etc.)
   ↓
Response returned to user
```

---

## 🧩 Components

### 1. Model

* TinyLlama (via Ollama or HuggingFace)

### 2. Agent Loop

* Prompt → decide tool → execute → respond

### 3. Tools (Skills)

* Calculator
* File reader
* (Optional) simple knowledge lookup

### 4. API Layer

* Lightweight server (FastAPI / Flask)
* `/query` endpoint

---

## 🚀 Quick Start

### 1. Install dependencies

```bash
pip install torch fastapi uvicorn
```

### 2. Run TinyLlama (Ollama example)

```bash
ollama run tinyllama
```

### 3. Start server

```bash
python server.py
```

### 4. Query the agent

```bash
curl -X POST http://localhost:8000/query \
     -H "Content-Type: application/json" \
     -d '{"query": "What is 45 * 23?"}'
```

---

## 🧪 Example Interaction

**Input**

```
"What is 45 * 23?"
```

**Agent reasoning (simplified)**

```
Tool: calculator
Input: 45 * 23
```

**Output**

```
1035
```

---

## 🧠 Design Principles

### 1. Minimalism

No frameworks. No abstractions unless necessary.

### 2. Observability

All steps are explicit:

* model output
* tool selection
* execution

### 3. Constraint-first

Built under:

* small model
* no APIs
* limited compute

---

## ⚠️ Limitations

* TinyLlama has limited reasoning depth
* Tool selection is prompt-sensitive
* No long-term memory (yet)

This is a **minimal working system**, not a production agent framework.

---

## 🔮 Extensions

* Add memory (vector store or simple cache)
* Improve tool selection via structured outputs
* Replace TinyLlama with larger local models
* Add domain-specific tools (e.g., telecom queries)

---

## 🧠 Why this matters

Running agents locally:

* reduces cost to near-zero
* improves privacy
* enables edge deployment

More importantly:

> It forces better system design under constraints

---

## 👤 Author

Joy Bose
Senior Data Scientist
PhD (Spiking Neural Networks)
