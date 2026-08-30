# 🤖 Multi-Agent AI System

A multi-agent AI application built with LangChain, Mistral AI, and FastAPI. It uses specialized agents, custom tools, and pipeline orchestration to process user queries and generate intelligent responses through a responsive web interface.

# ✨ Features
🤖 Multi-agent AI architecture
🧠 Mistral AI integration
🔗 LangChain agent orchestration
🛠️ Custom tools
🔍 Tavily web search
⚡ FastAPI backend
🌐 HTML, CSS & JavaScript frontend
📡 Frontend–backend API communication
🏗️ Project Structure
Multi_agent_system/
│
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── agents.py
├── pipeline.py
├── tools.py
├── main.py
├── requirements.txt
└── .gitignore
🛠️ Tech Stack

Backend: Python, FastAPI, Uvicorn
AI: LangChain, Mistral AI
Tools: Tavily Search
Frontend: HTML, CSS, JavaScript

# ⚙️ Setup

Clone the repository:

git clone https://github.com/YOUR_USERNAME/multi-agent-ai-system.git
cd multi-agent-ai-system

Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Create a .env file:

MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
▶️ Run

Start the FastAPI server:

uvicorn main:app --reload

Open:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs
👨‍💻 Author

Uttam Singh

© 2026 Uttam Singh
