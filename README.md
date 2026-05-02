# 🔬 ResearchMind – Multi-Agent AI Research System

ResearchMind is an end-to-end **multi-agent AI system** that automates the process of researching a topic, extracting insights, generating a structured report, and critically evaluating it.

Built with **LangChain and Streamlit**, this project demonstrates how multiple AI agents can collaborate to perform complex tasks efficiently.

---

## 🚀 Features

* 🔍 **Search Agent** – Retrieves relevant and up-to-date information from the web
* 📄 **Reader Agent** – Scrapes and extracts detailed content from selected sources
* ✍️ **Writer Agent** – Generates a structured research report
* 🧐 **Critic Agent** – Reviews and scores the generated report
* 🌐 **Interactive UI** – Built using Streamlit for a smooth user experience

---

## 🧠 Workflow

User input flows through a multi-agent pipeline:

```
User Input
   ↓
Search Agent
   ↓
Reader Agent
   ↓
Writer Agent
   ↓
Critic Agent
   ↓
Final Report + Feedback
```

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **OpenAI API**
* **Tavily API**
* **BeautifulSoup**
* **Requests**

---

## 📂 Project Structure

```
├── app.py            # Streamlit frontend
├── agents.py         # Agent setup and LLM configuration
├── tools.py          # Web search and scraping tools
├── pipeline.py       # CLI pipeline (optional)
├── requirements.txt  # Dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/researchmind.git
cd researchmind
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add environment variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push your project to GitHub
2. Go to Streamlit Cloud
3. Deploy your repository
4. Add secrets in **Settings → Secrets**:

```
OPENAI_API_KEY = "your_openai_api_key"
TAVILY_API_KEY = "your_tavily_api_key"
```

---

## 🎯 Use Cases

* Automated research and report generation
* Academic and technical writing assistance
* Market and trend analysis
* Learning multi-agent AI systems

---

## 🔒 Security

* `.env` file is excluded using `.gitignore`
* API keys are securely handled using Streamlit Secrets

---

##Outputs

<p align="center">
  <img src="Screenshot 2026-04-16 190949.png" width="800"/>
</p>

## 💡 Future Improvements

* Add memory between agents
* Integrate vector database (RAG)
* Export reports as PDF
* Improve scraping and source ranking

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/Kreezon

---

## ⭐ If you found this useful, consider giving it a star!

"# ResearchMind-2.0" 
