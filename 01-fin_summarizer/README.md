
# 💹 FinSummarizer – AI-Powered Financial Report Summarizer

FinSummarizer is a **Generative AI-powered tool** that ingests complex financial datasets (CSV format) and automatically generates **concise, human-readable summaries**.  
It helps **finance professionals, product teams, and decision-makers** quickly understand trends, anomalies, and key metrics without manually parsing large datasets.

This project is designed to **showcase end-to-end AI Product Management skills**, combining **technical AI implementation** with **PM artifacts** such as a sanitized PRD, KPIs, and deployment strategy.

---

## 🚀 Key Features
- **Automated Financial Summarization** using LLMs via LangChain.
- **Upload CSV Files** to analyze and summarize financial datasets.
- **Interactive Dashboard** built with Streamlit for seamless visualization.
- **Download Summaries** as CSV or text reports.
- **Scalable Deployment** using Docker and Streamlit Cloud.

---

## 🗂 Problem Statement

> Financial analysts and decision-makers spend countless hours reviewing spreadsheets and reports to identify key insights.  
>  
> **Problem:**  
> Large financial datasets are complex and time-consuming to analyze manually.  
> **Solution:**  
> FinSummarizer leverages **Large Language Models (LLMs)** to automatically generate **executive-ready summaries**, accelerating decision-making while reducing manual effort.

### **Primary KPIs**
| KPI | Target Value | Why It Matters |
|---|--------------|----------------|
| Summarization Accuracy | > 80% | Ensures the summaries are reliable for decision-making. |
| Processing Speed | < 10 sec for 1MB CSV | Smooth user experience. |
| User Satisfaction | 4.5/5+ | Measured via feedback form. |


## 🔄 High-Level Flow
```text
1. User Uploads CSV → Upload dataset of financial records.
2. Data Preprocessing → Clean and validate uploaded data.
3. LLM Summarization → Generate summaries using LangChain + LLM.
4. Post-Processing → Improve clarity, structure, and readability.
5. Dashboard Output → Streamlit displays summaries with download option.
6. User Downloads CSV → Summaries saved in a downloadable format.
```

---

## 📂 Folder Structure
```
FinSummarizer/
│
├── README.md                # Main project readme
├── requirements.txt         # Python dependencies
├── app.py                    # Streamlit web app
│
├── config/
│   └── config.yaml           # Model configs (sample only, no secrets)
│
├── data/
│   ├── sample_input.csv      # Example financial dataset
│   └── processed/            # Pre-processed datasets
│
├── src/
│   ├── data_preprocessing.py # Data cleaning scripts
│   ├── llm_integration.py    # LangChain + LLM logic
│   └── summarizer.py         # Core summarization pipeline
│
├── docs/
│   ├── PRD.md                # Public sanitized PRD
│   ├── Architecture_Diagram.png
│   └── Flowchart.png
│
├── tests/
│   ├── test_data_pipeline.py
│   └── test_summary_output.py
│
└── deployment/
    ├── streamlit_app.py      # Web deployment code
    └── Dockerfile
```

---

## 🛠️ Tech Stack
| Category       | Tools / Frameworks |
|---|--------------|
| **Language**   | Python 3.11 |
| **LLM Framework** | LangChain |
| **Generative AI Models** | OpenAI GPT-4 or Anthropic Claude |
| **Web Framework** | Streamlit |
| **Deployment** | Hugging Face Spaces / Streamlit Cloud |
| **Version Control** | Git + GitHub |
| **Containerization** | Docker |


## ⚙️ Installation & Setup

### **Prerequisites**
- Python 3.11+
- OpenAI API Key (or other LLM provider)
- Git installed

### **Steps**
```bash
# 1. Clone the repository
git clone https://github.com/vedika2609/ai_pm_developer_portfolio.git
cd 01-fin_summarizer

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
```

---

## 🧪 Testing
```bash
# Run all unit tests
pytest tests/
```

Example tests included:
- `test_data_pipeline.py` – Validates preprocessing logic.
- `test_summary_output.py` – Checks summarization quality.

---

## 🌟 Future Improvements
- Support **multilingual summarization** (e.g., Hindi, Spanish).
- Build **trend detection and anomaly insights** in addition to summaries.
- Integrate with **financial APIs** (e.g., Bloomberg, Yahoo Finance).
- Add **user authentication** and role-based access control.
- Deploy on a **scalable AWS architecture** for enterprise readiness.

---

## 📊 PM Deliverables
This project also demonstrates **AI Product Management skills** by including:
- **Sanitized PRD** (`docs/PRD.md`) → Showcases requirement gathering and scoping.
- **KPI Definition Table** → Metrics to track success.
- **Deployment Roadmap** → Clear steps to scale the product.

---

## 🚀 Deployment
Easily deploy to **Streamlit Cloud**:
```bash
streamlit run app.py
```

Or use **Docker** for containerized deployment:
```bash
docker build -t finsummarizer .
docker run -p 8501:8501 finsummarizer
```

---

## 👤 Author
**Vedika Gupta**  
AI Product Manager | Building Generative AI Systems  
- GitHub: [github.com/vedika-gupta](https://github.com/vedika2609)  
- LinkedIn: [linkedin.com/in/vedika-gupta](htpps://www.linkedin.com/in/vedika26gupta)

---

## 📜 License
This project is released under the **MIT License**.  
You are free to use, modify, and distribute this software with attribution.

---

## 🙌 Acknowledgements
- [LangChain](https://www.langchain.com/) – Framework for LLM-powered apps.
- [OpenAI](https://openai.com/) – Generative AI models.
- [Streamlit](https://streamlit.io/) – Rapid prototyping of data apps.

---

## 🌐 Live Demo
Coming soon: [Live Streamlit App](https://finsummarizer.streamlit.app)
