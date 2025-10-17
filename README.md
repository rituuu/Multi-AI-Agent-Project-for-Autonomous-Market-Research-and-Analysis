
# Multi-Agent System for AI-Powered Market Research, Use Case Generation, and Resource Collection

An **intelligent multi-agent system** that automates **market research, AI use-case generation, and resource asset discovery** using orchestrated **LLM-driven agents** built with **LangGraph**, **LangChain**, and **Gradio**.

This project demonstrates how multiple AI agents can collaboratively reason, research, and produce actionable business intelligence — exactly the kind of applied AI system recruiters and organizations are looking for today.

---

## Project Overview

Modern AI solutions demand systems that **think, research, and plan autonomously** across multiple stages.
This project builds a **three-agent orchestration pipeline** capable of:

1. **Market Research Agent** → Conducts in-depth industry or company analysis, trends, and competitor mapping.
2. **AI Use Case Generation Agent** → Synthesizes insights into relevant, innovative AI/ML/Automation use cases.
3. **Resource Collection Agent** → Gathers datasets, tools, frameworks, and APIs aligned with proposed use cases.

All agents interact dynamically through a **LangGraph-based state machine**, creating a continuous feedback loop that mimics real-world analyst collaboration.

## Key Features

### Multi-Agent Collaboration

* Each agent has a unique goal and prompt configuration.
* Information flows between agents via shared state, enabling contextual reasoning.
* Autonomous decision flow handled by **LangGraph**.

### Automated Market Research

* Uses integrated search tools to analyze companies, industries, and competitors.
* Extracts insights on market trends, segmentation, and challenges.
* Produces detailed industry overviews for decision support.

### AI/ML/Automation Use Case Generation

* Generates actionable AI and GenAI use cases tailored to industry pain points.
* Identifies potential applications across business functions (Operations, Supply Chain, Customer Experience, etc.).
* Outputs results in a structured, implementation-ready format.

### Resource Discovery & Knowledge Assets

* Finds datasets, pre-trained models, APIs, and frameworks related to each use case.
* Suggests practical GenAI solutions such as:

  * Document Search Systems
  * Automated Report Generation
  * AI-Powered Chat Systems
* Saves all results in a time-stamped Markdown file for reproducibility.

### Real-World Application

Perfect for demonstrating skills in **Agentic AI, Market Intelligence, LangGraph orchestration, and LLM workflow automation** — highly demanded areas in enterprise AI and GenAI roles.

## Project Structure: 
│
├── app/ <br>
│   └── backend/ <br>
│       ├── __init__.py <br>
│       └── fastapi_app.py      # your FastAPI app <br>
│
├── agents/ <br>
│   ├── __init__.py <br>
│   └── MultiAgents.py         # your multi-agent workflow <br>
│
├── frontend/ <br>
│   ├── __init__.py <br>
│   └── ui.py                  # Gradio frontend <br>
│
├── common/  <br>
│   ├── __init__.py <br>
│   ├── logger.py <br>
│   └── custom_exception.py  <br>
│
├── configuration/  <br>
│   ├── __init__.py  <br>
│   └── config.py              # settings object   <br>
│
├── output/                    # resources will be saved here   <br>
│
├── .env  <br>
├── requirements.txt  <br>
└── README.md   <br>


## Architecture

```
                ┌────────────────────────────────────────────┐
                │           Market Research Agent            │
                │  • Analyzes industry & competitors         │
                │  • Uses web search tools                   │
                └────────────────────────────────────────────┘
                                │
                                ▼
                ┌────────────────────────────────────────────┐
                │         AI Use Case Generation Agent       │
                │  • Reads research results                  │
                │  • Proposes AI/ML/Automation applications  │
                │  • Generates structured insights           │
                └────────────────────────────────────────────┘
                                │
                                ▼
                ┌────────────────────────────────────────────┐
                │        Resource Collection Agent           │
                │  • Collects datasets, APIs, tools          │
                │  • Suggests GenAI frameworks               │
                │  • Saves results to Markdown output        │
                └────────────────────────────────────────────┘
```

All three are orchestrated through a **LangGraph StateGraph**, maintaining a shared state of `messages` and looping until insights are complete.

---

## Tech Stack

| Layer                      | Technology / Tool                          | Purpose                                                        |
| -------------------------- | ------------------------------------------ | -------------------------------------------------------------- |
| **LLM Interface**          | LangChain + LangGraph                      | Multi-agent orchestration & message state management           |
| **Model Backend**          | LLM (Generic / Gemini / OpenAI compatible) | Natural language reasoning & generation                        |
| **Web Framework**          | Gradio                                     | Interactive front-end for query input and output visualization |
| **Search Tool**            | Tavily API                                 | Web-based search for live industry and company data            |
| **Environment Management** | Conda / Virtualenv                         | Isolated reproducible Python environment                       |
| **Logging**                | Python `logging`                           | Workflow traceability and debugging                            |

---

## How It Works (Pipeline Flow)

1. **User Query Input**
   The user enters a company or industry (e.g., “FinTech in Asia” or “Tesla”).

2. **Agent 1: Market Research**

   * Performs structured research using integrated tools.
   * Summarizes industry overview, challenges, trends, and competitors.

3. **Agent 2: AI/ML Use Case Generator**

   * Reads Agent 1’s output.
   * Creates AI/ML/GenAI-based solutions addressing pain points.
   * Outputs creative and relevant use cases.

4. **Agent 3: Resource Collector**

   * Maps each use case to supporting datasets, APIs, and models.
   * Suggests actionable GenAI solutions.
   * Saves all resources into a Markdown file with a timestamp.

5. **Gradio Interface**

   * Displays progress step-by-step (“Researching…”, “Generating Use Cases…”, “Collecting Resources…”).
   * Shows full final outputs neatly in Markdown.

---

## Output Example

Each run generates a full insight report saved as:

```
/output/resources_YYYYMMDD_HHMMSS.md
```

Containing:

* Market Research Summary
* Generated Use Cases
* Datasets, APIs & Tools for Each Use Case

This output can be shared directly in professional reports, dashboards, or research presentations.

---

## Installation & Usage

### Clone the Repository

```bash
git clone https://github.com/rituuu/multi-agent-market-research.git
cd multi-agent-market-research
```

### 1.	Create a conda environment
conda create -p venv python==3.11.13 –y

### 2.	Activate conda environment
conda activate venv

### 3.	After activating we will install this requirements.txt

pip install –r requirements.txt

### 4. Set Up Environment Variables

Create a `.env` file with your API keys:

```bash
TAVILY_API_KEY=your_tavily_key
GOOGLE_API_KEY=your_google_key
```

### 5. Run the Application

```bash
python frontend/ui.py
```

### Launch Interface

Gradio will open automatically in your browser at:

http://127.0.0.1:7860


## Sample Query

> “Generate AI market insights and automation use cases for the global healthcare industry.”

**Output includes:**

* Detailed healthcare industry analysis
* AI/ML/Automation opportunities
* Competitor landscape
* Datasets and frameworks for implementation

---

## What This Project Demonstrates

End-to-end orchestration of autonomous AI agents <br>
Expertise in LangGraph, LangChain, and LLM workflows <br>
Business-aligned reasoning & multi-stage task automation <br>
Strong grasp of AI product ideation and research automation <br>
Portfolio-ready system demonstrating Agentic AI in action <br>

## Future Improvements

* Integrate vector databases for memory persistence <br>
* Add visualization dashboards for use-case mapping <br>
* Support for additional LLMs and reasoning agents <br>
* API deployment for enterprise use <br>

## Ideal For

**AI Research & Innovation Roles**
**Data Science / AI Product Engineer Portfolios**
**Agentic AI & Multi-Agent Systems Demonstration Projects**

---

**Author:** RITU GUJELA
**Tech Stack:** Python • LangChain • LangGraph • Gradio • Tool Integration • FastAPI 
**License:** MIT

---
