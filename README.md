🤖 Multi-Agent AI System

A full-stack multi-agent AI application built with Python, FastAPI, LangChain, and Mistral AI. The system uses multiple specialized AI agents, custom tools, web search, and pipeline-based orchestration to process user queries and generate intelligent responses through a modern web interface.

✨ Features
🤖 Multi-Agent AI Architecture
🧠 Mistral AI for intelligent language processing
🔗 LangChain for agent and LLM orchestration
⚡ FastAPI backend
🛠️ Custom AI Tools
🔍 Tavily Web Search
🔄 Agent Pipeline Orchestration
🌐 HTML, CSS & JavaScript Frontend
📡 REST API communication
📚 Automatic FastAPI API Documentation
🔐 Environment variable support
📱 Responsive Web Interface
🏗️ Project Architecture
                         ┌───────────────────┐
                         │       USER        │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   Web Frontend    │
                         │   HTML/CSS/JS     │
                         └─────────┬─────────┘
                                   │
                              HTTP Request
                                   │
                                   ▼
                         ┌───────────────────┐
                         │      FastAPI      │
                         │      Backend      │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │     Pipeline      │
                         │   Orchestrator    │
                         └─────────┬─────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    ▼              ▼              ▼
             ┌────────────┐ ┌────────────┐ ┌────────────┐
             │   Agent 1  │ │   Agent 2  │ │   Agent 3  │
             └──────┬─────┘ └──────┬─────┘ └──────┬─────┘
                    │              │              │
                    └──────────────┼──────────────┘
                                   ▼
                         ┌───────────────────┐
                         │   Custom Tools    │
                         │  + Tavily Search  │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │     Mistral AI    │
                         │       LLM         │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │  Final Response   │
                         └───────────────────┘
📁 Project Structure
Multi_agent_system/
│
├── static/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── agents.py
├── main.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
📂 File Description
File	Description
main.py	FastAPI backend and API endpoints
agents.py	Defines and configures AI agents
pipeline.py	Handles agent orchestration and workflow
tools.py	Contains custom tools used by agents
requirements.txt	Python project dependencies
static/index.html	Frontend application structure
static/style.css	Frontend styling
static/script.js	Frontend logic and API communication
.gitignore	Prevents secrets, virtual environments and temporary files from being committed
.env	Stores API keys and environment variables
🛠️ Technologies Used
Backend
🐍 Python
⚡ FastAPI
🔗 LangChain
🧠 Mistral AI
🔍 Tavily Search
🔐 python-dotenv
🚀 Uvicorn
Frontend
🌐 HTML5
🎨 CSS3
⚙️ JavaScript
🧠 Multi-Agent System

The application follows a multi-agent architecture where different agents can be assigned different responsibilities.

Instead of relying on a single AI agent to perform every task, the system separates responsibilities between specialized agents.

User Query
    │
    ▼
Agent Pipeline
    │
    ├──► Specialized Agent
    │
    ├──► Tool-Using Agent
    │
    └──► Response Agent
             │
             ▼
        Final Response

This approach makes the application easier to extend and maintain.

🔄 Agent Pipeline

The agent workflow is implemented in:

pipeline.py

The pipeline controls how information flows between the different agents.

A typical workflow can be represented as:

User Query
    ↓
Analyze Query
    ↓
Select Appropriate Agent
    ↓
Execute Required Tools
    ↓
Process Information
    ↓
Generate Final Response
    ↓
Return Response to User

The architecture can be extended by adding new agents or tools without redesigning the entire application.

🛠️ Custom Tools

Custom tools are implemented in:

tools.py

Tools allow AI agents to perform actions beyond normal text generation.

For example, agents can use external search capabilities through Tavily Search to retrieve current information from the web.

AI Agent
    │
    ▼
Decides Tool Is Required
    │
    ▼
Custom Tool
    │
    ▼
External Information
    │
    ▼
Agent Processes Result
🔍 Web Search

The system can integrate Tavily Search as a tool for retrieving information from the web.

This allows agents to handle queries where external or recent information may be required.

Note: A Tavily API key is required to use Tavily-powered search functionality.

⚡ FastAPI Backend

The backend is powered by FastAPI.

The main backend application is:

main.py

FastAPI handles:

API requests
User queries
Communication with the AI pipeline
Returning responses to the frontend
Backend application routing
📡 API Documentation

FastAPI automatically provides interactive API documentation.

After starting the server, open:

http://127.0.0.1:8000/docs

You can also access the alternative documentation at:

http://127.0.0.1:8000/redoc

The Swagger UI can be used to test API endpoints directly from the browser.

🌐 Frontend

The frontend is located inside the:

static/

directory.

index.html

Contains the structure of the web application.

style.css

Contains the visual design and responsive styling.

script.js

Handles frontend interactions and communication with the FastAPI backend.

The overall communication flow is:

Browser
   │
   │ HTTP Request
   ▼
FastAPI Backend
   │
   ▼
Multi-Agent Pipeline
   │
   ▼
Mistral AI / Tools
   │
   ▼
FastAPI Response
   │
   ▼
Browser
⚙️ Installation
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/multi-agent-ai-system.git

Move into the project directory:

cd multi-agent-ai-system
🐍 2. Create a Virtual Environment

Create a Python virtual environment:

python -m venv .venv
Windows

Activate the environment:

.venv\Scripts\activate
Linux / macOS
source .venv/bin/activate
📦 3. Install Dependencies

Install all required Python packages:

pip install -r requirements.txt
🔐 4. Configure Environment Variables

Create a .env file in the project root:

MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key

Replace the values with your own API keys.

⚠️ Important

Never commit your .env file to GitHub.

Your .gitignore should contain:

.env
.venv/
__pycache__/
*.pyc

For sharing the required environment variables with other developers, you can create:

.env.example

Example:

MISTRAL_API_KEY=your_mistral_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
▶️ Running the Application

Make sure your virtual environment is activated.

Start the FastAPI server using:

uvicorn main:app --reload

The backend will start at:

http://127.0.0.1:8000

Open the application in your browser.

🧪 Testing the API

FastAPI provides an interactive Swagger interface.

Open:

http://127.0.0.1:8000/docs

From there you can:

Select an API endpoint.
Click Try it out.
Enter the required request data.
Execute the request.
View the response.
🔑 API Keys

This project may require API keys for external AI and search services.

Service	Environment Variable
Mistral AI	MISTRAL_API_KEY
Tavily	TAVILY_API_KEY

Keep these keys private.

Do not upload API keys directly into Python files or GitHub.

📌 Why Multi-Agent AI?

A multi-agent architecture can provide several advantages:

Specialization — each agent can focus on a particular task.
Modularity — agents and tools can be added independently.
Scalability — workflows can grow as new capabilities are introduced.
Tool Integration — agents can interact with external tools.
Better Organization — complex workflows can be divided into smaller steps.
🚀 Future Improvements

Possible future improvements include:

 Add more specialized agents
 Implement agent memory
 Add conversation history
 Add streaming responses
 Improve agent routing
 Add parallel agent execution
 Add more custom tools
 Add authentication
 Add database support
 Add production deployment
 Improve error handling
 Add automated testing
🔒 Security

For production deployments:

Store API keys using environment variables or a secrets manager.
Never expose .env files publicly.
Never hard-code API keys.
Validate incoming API requests.
Configure appropriate CORS policies.
Add authentication where required.
Use HTTPS in production.
📚 Learning Goals

This project demonstrates practical concepts including:

Large Language Models (LLMs)
AI Agents
Multi-Agent Systems
Tool Calling
LangChain
Mistral AI
FastAPI
REST APIs
Web Search Integration
Frontend–Backend Communication
AI Workflow Orchestration
🤝 Contributing

Contributions are welcome!

To contribute:

git clone https://github.com/YOUR_USERNAME/multi-agent-ai-system.git
cd multi-agent-ai-system

Create a new branch:

git checkout -b feature/new-feature

Make your changes and commit them:

git add .
git commit -m "Add new feature"

Push your branch:

git push origin feature/new-feature

Then open a Pull Request.

📜 License

This project is intended for educational and development purposes.

You can add an appropriate open-source license such as MIT License if you want others to freely use and modify the project.

👨‍💻 Author
Uttam Singh

Built with ❤️ using:

Python • FastAPI • LangChain • Mistral AI • Tavily • HTML • CSS • JavaScript

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!

© 2026 Uttam Singh
