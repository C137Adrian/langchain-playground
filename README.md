🚀 LangChain Playground
Llama 3.1 + Groq

A minimal and well-structured foundation for building applications with LangChain, powered by Llama 3.1 models served through Groq.

This repository is designed as a clean, modular, and extensible environment for building:

🔗 Chains

🤖 Agents

🛠️ Tools

🧪 Rapid prototypes

📦 Installation

Clone the repository and navigate into the project directory:

git clone https://github.com/yourusername/langchain-playground.git
cd langchain-playground


Install dependencies:

pip install -r requirements.txt

⚙️ Configuration

The project uses environment variables to manage credentials.

Create a .env file in the root directory.

Follow the format defined in .env.example:

GROQ_API_KEY=your_api_key

▶️ Usage

Run the application with:

python src/main.py

🗂️ Project Structure
src/
│
├── agents/      # Agent definitions
├── chains/      # Chain implementations
├── utils/       # Utilities and helper functions
└── main.py      # Application entry point

tests/           # Automated tests
.env.example     # Environment variables template
requirements.txt # Project dependencies

🎯 Project Goals

Provide a solid foundation for rapid experimentation with LangChain

Enable seamless extension into agents, tools, and complex workflows

Maintain a clean, modular, and scalable architecture from the start

Serve as a reusable template for future LLM-based projects

📜 License

This project is licensed under the MIT License.