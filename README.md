# 🚀 AI Job Posting Generator

An end-to-end AI-powered system that generates professional job postings using a multi-agent architecture. Built with CrewAI, FastAPI, and Supabase.

---

## 📌 Features

* 🤖 Multi-agent AI system using CrewAI
* 🧠 Automated job description generation
* 🌐 Web interface for user input
* 🗄️ Database integration using Supabase
* ⚡ FastAPI backend for API handling

---

## 🏗️ Tech Stack

* Backend: Python, FastAPI
* AI Framework: CrewAI
* LLM: OpenAI API
* Database: Supabase
* Frontend: HTML, JavaScript

---

## 🧠 Architecture

Frontend → FastAPI → CrewAI Agents → OpenAI → Supabase

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/ai-job-generator.git
cd ai-job-generator
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Setup Environment Variables

Create `.env` file:

```
OPENAI_API_KEY=your_api_key
SUPABASE_URL=your_url
SUPABASE_KEY=your_key
```

---

### 4. Run Backend

```bash
uvicorn job_posting.api:app --reload
```

---

### 5. Open Frontend

Open `frontend.html` in browser

---

## 🧪 Usage

1. Enter company name and job role
2. Click "Generate"
3. AI generates job description
4. Data is stored in Supabase

---

## ⚠️ Note

This project requires OpenAI API credits. If quota is exceeded, generation may fail.

---

## 🚀 Future Improvements

* React-based frontend UI
* Authentication system
* Salary prediction feature
* Deployment on cloud (Render/Vercel)

---

## 👨‍💻 Author

Your Name

---

## 📜 License

MIT License
