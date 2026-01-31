# AI Research Agent

This project implements a tool-using AI research agent that transforms an open-ended research prompt into a structured, evidence-backed Markdown research report.

Instead of relying solely on model knowledge, the agent performs grounded reasoning by searching the web, retrieving sources, extracting structured evidence, and synthesizing findings.

---

## Project Structure

research_agent/
├── agent/                 # Core agent logic  
│   ├── planner.py  
│   ├── search_tool.py  
│   ├── retriever.py  
│   ├── extractor.py  
│   ├── research_agent.py  # Entry point  
│   └── __init__.py  
│
├── reports/               # Generated research reports  
│   └── research_report.md  
│
├── writeup.md             # Design proposal  
├── requirements.txt  
└── .gitignore  

---

## Setup

1. Clone the repository:
2. Install dependencies:
3. Create a `.env` file in the project root:
OPENAI_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
4. pip install -r requirements.txt




---

## How to Run the Agent

From the project root directory, run:

python -m agent.research_agent


The agent will:

1. Plan research tasks  
2. Search the web  
3. Retrieve relevant pages  
4. Extract structured evidence  
5. Generate a Markdown research report  

---

## Output

The generated research report will be saved to:


---


---

## What This Project Demonstrates

- Tool-using AI agent architecture  
- Multi-step reasoning loops  
- Structured intermediate representations to reduce hallucination  
- Traceability between claims and sources  
- Modular, scalable project structure  
- Real-world web interaction with error handling  