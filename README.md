# 🤖 Multi-Agent Research System

A production-ready **Multi-Agent AI Research System** built using **LangGraph**, **OpenAI-compatible LLMs**, **RAG**, **FastAPI**, and **Streamlit**. The system uses multiple specialized AI agents to collaboratively research topics, retrieve information, verify facts, and generate comprehensive reports.

---

## 🚀 Features

* 🧠 Planner Agent for task decomposition
* 🔍 Web Search Agent for online research
* 📄 PDF/RAG Agent for document retrieval
* 🗄️ SQL Agent for structured database queries
* 📊 Analysis Agent for summarizing and comparing findings
* ✅ Fact Checker Agent for source verification
* ✍️ Writer Agent for report generation
* 📝 Reviewer Agent for quality improvement
* 💾 Vector Database integration (Chroma/FAISS)
* 🌐 FastAPI REST API
* 🎨 Streamlit user interface

---

## 🏗️ System Architecture

```text
                User
                  │
                  ▼
          Supervisor Agent
                  │
         Planner Agent
                  │
     ┌────────┬─────────┬─────────┐
     ▼        ▼         ▼         ▼
 Search    PDF/RAG     SQL     Web Tools
  Agent     Agent      Agent
     └────────┴─────────┴─────────┘
                  │
                  ▼
           Analysis Agent
                  │
                  ▼
         Fact Checker Agent
                  │
                  ▼
            Writer Agent
                  │
                  ▼
           Reviewer Agent
                  │
                  ▼
             Final Report
```

---

## 📂 Project Structure

```text
multi-agent-research/
│
├── agents/
├── api/
├── config/
├── data/
├── frontend/
├── tools/
├── workflows/
├── tests/
├── logs/
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🛠️ Tech Stack

### AI & LLM

* Python
* LangGraph
* OpenAI Agents SDK (optional)
* Hugging Face Transformers

### Retrieval

* LangChain
* ChromaDB / FAISS
* Sentence Transformers

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Database

* SQLite / PostgreSQL

### Utilities

* PyMuPDF
* Pandas
* NumPy

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/multi-agent-research.git

cd multi-agent-research
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file.

```env
OPENAI_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
```

---

## ▶️ Run the Project

### Start FastAPI

```bash
uvicorn api.routes:app --reload
```

### Start Streamlit

```bash
streamlit run frontend/streamlit_app.py
```

---

## 🔄 Workflow

1. User submits a research query.
2. Planner Agent breaks the task into smaller subtasks.
3. Search, PDF/RAG, and SQL agents gather relevant information.
4. Analysis Agent synthesizes the collected data.
5. Fact Checker validates important claims.
6. Writer Agent produces a structured report.
7. Reviewer Agent improves clarity, consistency, and formatting.
8. The final report is returned to the user.

---

## 📌 Example Query

```
Compare GPT-5, Claude, and Gemini for software engineering tasks.
```

### Output

* Executive Summary
* Feature Comparison
* Performance Analysis
* Strengths and Weaknesses
* References
* Final Recommendation

---

## 🧪 Future Improvements

* Human-in-the-loop approval
* Multi-modal document support
* Long-term memory
* Multi-language research
* Agent performance monitoring
* Docker deployment
* Kubernetes support
* CI/CD pipeline

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---




---

##  Acknowledgements

* LangGraph
* LangChain
* OpenAI
* Hugging Face
* ChromaDB
* FastAPI
* Streamlit
