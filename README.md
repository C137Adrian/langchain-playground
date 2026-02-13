# 🚀 LangChain Playground

<p align="center">
  <strong>Llama 3.1 + Groq</strong>
</p>

---

A minimal and well-structured foundation for building applications with **LangChain**, powered by **Llama 3.1** models served through **Groq**.

This repository provides a clean, modular, and extensible environment for building:

- 🔗 **Chains**
- 🤖 **Agents**
- 🛠️ **Tools**
- 🧪 **Rapid Prototypes**

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/langchain-playground.git
cd langchain-playground
```

### 2. Install dependencies

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

## 🗂️ Project Structure

```text
src/
│
├── agents/      # Agent definitions
├── chains/      # Chain implementations
├── utils/       # Utilities and helpers
└── main.py      # Application entry point

tests/           # Automated tests
.env.example     # Environment variables template
requirements.txt # Project dependencies
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
