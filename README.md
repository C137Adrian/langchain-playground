# 🚀 LangChain Playground

### Llama 3.1 + Groq

---

A minimal and well-structured foundation for building applications with **LangChain**, powered by **Llama 3.1** models served through **Groq**.

This repository provides a clean, modular, and extensible environment for building:

- 🔗 **Chains**
- 🤖 **Agents**
- 🛠️ **Tools**
- 🧪 **Rapid Prototypes**

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/langchain-playground.git
cd langchain-playground
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

The project uses environment variables to manage credentials.

### 1. Create a `.env` file in the root directory

### 2. Add your Groq API key (see `.env.example`)

```env
GROQ_API_KEY=your_api_key
```

---

## ▶️ Usage

Run the application:

```bash
python src/main.py
```

---

## 🧱 LangChain Compatibility Notes

This project uses:

- `langchain`
- `langchain-core`
- `langchain-classic` (for compatibility with the original Quickstart API)
- `langchain-groq`

LangChain is currently transitioning to a new architecture based on **Runnables**.  
To keep Quickstart examples stable and predictable, this project uses:

- `LLMChain`
- `SequentialChain`
- `ConversationChain`
- `ConversationBufferMemory`

These come from `langchain-classic`, which preserves the original LangChain API.  
A future branch will migrate the project to the modern Runnable-based architecture.

---

## 🗂️ Project Structure

```
src/
│
├── agents/      # Agent definitions
├── chains/      # Chain implementations (basic, sequential, memory…)
├── utils/       # Utilities and helpers
└── main.py      # Application entry point

.env.example     # Environment variables template
requirements.txt # Project dependencies
LICENSE          # Project license
README.md        # Project documentation
```

---

## 🎯 Project Goals

- Provide a solid foundation for rapid experimentation  
- Enable seamless extension into agents, tools, and complex workflows  
- Maintain a clean, modular, and scalable architecture  
- Serve as a reusable template for future LLM-based projects  

---

## 📜 License

This project is licensed under the **MIT License**.
