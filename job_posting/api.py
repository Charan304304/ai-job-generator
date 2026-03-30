from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from job_posting.crew import JobPostingCrew
from job_posting.db import supabase
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# ✅ CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model
class JobRequest(BaseModel):
    company: str
    role: str


# Save function
def save_job(company, role, description):
    supabase.table("job_posts").insert({
        "company": company,
        "role": role,
        "description": description
    }).execute()


@app.post("/generate-job")
def generate_job(data: JobRequest):
    try:
        inputs = {
            'company_domain': data.company,
            'company_description': f"{data.company} is a company.",
            'hiring_needs': data.role,
            'specific_benefits': "Standard benefits"
        }

        crew = JobPostingCrew().crew()

        # Run AI
        result = crew.kickoff(inputs=inputs)

        result_text = str(result)

        # Save to DB
        save_job(data.company, data.role, result_text)

        return {"job_post": result_text}

    except Exception as e:
        # Return error instead of crashing
        return {"error": str(e)}