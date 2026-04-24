# IntelLyst – Multi-Agent Research Orchestrator

## 🧩 Overview
IntelLyst is an **AI-powered, multi-agent research assistant** that autonomously retrieves, analyzes, and synthesizes data from multiple sources to deliver concise insights.

It showcases **LangGraph-based orchestration**, where agents collaborate (Retriever, Summarizer, Comparator) — mirroring MCP-style coordination.

## 🗂 Problem Statement
Modern professionals spend excessive time gathering, synthesizing, and comparing research from multiple sources. IntelLyst solves this by deploying **collaborative AI agents** that emulate a research team—each agent specializing in data retrieval, summarization, or comparative analysis—to produce decision-ready insights in seconds.

**Objective:** Reduce research and synthesis time by **70%** while maintaining summary relevance ≥4.5/5.

## 🎯 Objective
Reduce research time by **70%** through AI agents that:
1. Retrieve relevant data.
2. Summarize findings.
3. Compare entities and highlight insights.

## 🧠 Architecture
```
User Query
   ↓
[Retriever Agent] → Finds data
   ↓
[Summarizer Agent] → Synthesizes points
   ↓
[Comparator Agent] → Analyzes differences
   ↓
Final Output → Streamlit Dashboard / JSON Report
```

## 🔁 High-Level Flow
1. User enters a research query (e.g., “Compare Nvidia and AMD AI growth strategies”).
2. Retriever Agent gathers data from APIs or datasets.
3. Summarizer Agent condenses data into readable summaries.
4. Comparator Agent evaluates and contrasts key insights.
5. Final report is generated, visualized in Streamlit, and exportable as a CSV or text file.

## ⚙️ Tech Stack
| Layer | Tool |
|-------|------|
| LLM | GPT-4 / Claude (AWS Bedrock) |
| Framework | LangChain + LangGraph |
| Memory | FAISS / Chroma |
| Frontend | Streamlit |
| Deployment | Hugging Face Spaces |

## 📊 Metrics
| KPI | Target |
|------|--------|
| Accuracy | ≥85% |
| Latency | ≤4s |
| Task Completion | ≥90% |
| Summary Relevance | ≥4.5/5 |

## 📂 Folder Structure
```
intelLyst/
├── README.md
├── app.py
├── src/
│   ├── retriever_agent.py
│   ├── summarizer_agent.py
│   ├── comparator_agent.py
│   └── orchestration.py
├── data/
│   ├── sample_queries.json
│   └── output/
├── docs/
│   ├── PRD.md
│   ├── Architecture.png
│   └── Flowchart.png
└── deployment/
    ├── streamlit_app.py
    └── Dockerfile
```

## 🚀 Quick Start
```bash
git clone https://github.com/vedika2609/ai_pm_developer_portfolio.git
cd 02-intelLyst
pip install -r requirements.txt
streamlit run app.py
```

## 🎥 Demo
➡️ [Live Demo on Hugging Face Spaces](#) (Coming soon)

## 💡 Future Enhancements
- Voice input (“Ask IntelLyst”)
- Multilingual summarization
- PDF document integration
- Explainability module

## 👤 Author
**Vedika Gupta**  
AI Product Manager | Building Generative AI Systems  
- GitHub: [github.com/vedika-gupta](https://github.com/vedika2609)  
- LinkedIn: [linkedin.com/in/vedika-gupta](https://www.linkedin.com/in/vedika26gupta/)
- 🖋️Blog: (Coming soon)