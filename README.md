# 🚀 LangChain Playground — Groq + Llama 3.1

---

A clean and modular foundation for building applications with **LangChain**, powered by **Llama 3.1** models served through **Groq**.

The project is designed for clarity, extensibility, and ease of experimentation, offering a modern implementation of:

- 🔗 Tool-driven agents  
- 🤖 Function-calling workflows  
- 📚 A complete RAG pipeline  
- 🛠️ Custom tools  
- ✅ A well-tested and production-ready architecture  

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/langchain-playground.git
cd langchain-playground
```

### 2. Create a Conda environment

```bash
conda create -n langchain-pro python=3.11 -y
conda activate langchain-pro
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

The project uses environment variables for credentials.

### 1. Copy the example file

```bash
cp .env.example .env
```

### 2. Add your Groq API key

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Usage

Run the terminal chat agent:

```bash
python src/main.py
```

### Example session

```
Agent ready. Type 'exit' to quit.

You: 5+5
Agent: 10
```

The agent automatically decides whether to:

- Answer directly  
- Call one of the registered tools  
- Use the RAG pipeline to retrieve contextual information  

---

## 🧠 Architecture Overview

The project follows the modern **LangChain** architecture, emphasizing clarity and forward compatibility.

### Key Components

- `@tool` decorators for defining tools  
- `llm.bind_tools()` for structured function calling  
- A custom multi-tool agent  
- A complete RAG pipeline (FAISS + embeddings + retriever)  
- A lightweight agent loop without legacy abstractions  

### Not Used

- Deprecated agents (`initialize_agent`)  
- Deprecated chains (`LLMChain`, `AgentExecutor`)  
- Legacy LangChain APIs  

The goal is to provide a stable, maintainable foundation suitable for real applications.

---

## 🗂️ Project Structure

```text
src/
│
├── agents/
│   └── multi_tool_agent.py     # Main multi-tool agent
│
├── tools/
│   ├── math_tools.py           # Arithmetic tools
│   ├── text_tools.py           # Text utilities
│   ├── time_tools.py           # Time utility
│   └── rag_tool.py             # RAG tool wrapper
│
├── rag/
│   ├── rag_search.py           # RAG retrieval pipeline
│   ├── retriever.py            # FAISS retriever logic
│   ├── vectorstore.py          # Vectorstore initialization
│   └── embeddings.py           # Embedding model configuration
│
├── llm/
│   └── groq.py                 # Groq LLM configuration
│
└── main.py                     # Terminal chat entry point

tests/
│   ├── unit/                   # Unit tests for tools and agent
│   └── integration/            # Integration tests (RAG + agent)

.env.example
requirements.txt
pytest.ini
README.md
```

---

## 🧪 Testing

The project includes a full test suite covering:

- Unit tests for all tools  
- Unit test for agent initialization  
- Integration test for the RAG pipeline and tool-calling behavior  

Run all tests:

```bash
pytest -q
```

A successful run should show:

```
10 passed, X warnings
```

---

## 🛠️ Extending the Project

To add a new tool:

1. Create a function in `src/tools/`  
2. Decorate it with `@tool`  
3. Import it in `multi_tool_agent.py`  
4. Add it to the tools list  
5. Write a unit test in `tests/unit/`  

### Example

```python
from langchain.tools import tool

@tool
def double(x: int) -> int:
    """Returns x * 2."""
    return x * 2
```

---

## 📚 RAG Pipeline

The RAG subsystem is fully modular:

- **Embeddings:** Sentence Transformers  
- **Vectorstore:** FAISS  
- **Retriever:** Top-k similarity search  
- **Tool:** `rag_tool` wraps the retrieval pipeline for the agent  

To rebuild the vectorstore:

```python
from src.rag.vectorstore import build_vectorstore
build_vectorstore()
```

---

## 🎯 Purpose

This repository provides a clear, maintainable starting point for:

- Building LangChain applications with Groq  
- Experimenting with tool-calling agents  
- Developing RAG-enhanced assistants  
- Creating production-ready AI services  

It is intentionally minimal, but structured to scale as your project grows.
