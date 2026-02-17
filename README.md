# 🚀 LangChain Playground — Groq + Llama 3.1

---

A minimal and well-structured foundation for building applications with **LangChain** using **Llama 3.1** models served through **Groq**.

This repository provides a clean, modular environment for:

- 🔗 **Tool-driven agents**
- 🤖 **Function-calling workflows**
- 🛠️ **Custom tools**
- ⚡ **Rapid prototyping**

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

**Example session:**

```
Agente listo. Escribe 'exit' para salir.

Tú: 5+5
Agente: 10
```

---

## 🧠 Architecture Notes

This project follows the **modern LangChain architecture**, using:

- `@tool` for defining tools  
- `llm.bind_tools()` for function calling  
- `ChatGroq` for Llama 3.1 models  
- A minimal custom agent loop  

Not used:

- Legacy agents (`initialize_agent`)  
- Legacy chains (`LLMChain`, `AgentExecutor`)  
- Deprecated LangChain APIs  

**Goal:** clarity, stability, and forward compatibility.

---

## 🗂️ Project Structure

```text
src/
│
├── agents/
│   └── multi_tool_agent.py     # Tool-calling agent
│
├── tools/
│   ├── math_tools.py           # Basic math operations
│   ├── text_tools.py           # Text utilities
│   └── time_tools.py           # Current time tool
│
├── llm/
│   └── groq.py                 # Groq model configuration
│
└── main.py                     # Terminal chat entry point

.env.example
requirements.txt
README.md
```

---

## 🛠️ Extending the Project

To add a new tool:

1. Create a file in `src/tools/`  
2. Decorate the function with `@tool`  
3. Add it to the tool list in `multi_tool_agent.py`  

**Example:**

```python
from langchain.tools import tool

@tool
def double(x: int) -> int:
    """Returns x * 2."""
    return x * 2
```

---

## 🎯 Purpose

- Provide a clean starting point for LangChain + Groq projects  
- Enable quick experimentation with tools and agents  
- Maintain a simple, readable, and scalable structure
