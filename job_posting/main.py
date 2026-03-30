from dotenv import load_dotenv
load_dotenv()

import sys
from job_posting.crew import JobPostingCrew
from job_posting.db import supabase


# Function to save job posting into Supabase
def save_job(company, role, description):
    supabase.table("job_posts").insert({
        "company": company,
        "role": role,
        "description": description
    }).execute()


def run():
    inputs = {
        'company_domain': 'careers.wbd.com',
        'company_description': "Warner Bros. Discovery is a premier global media and entertainment company, offering audiences the world’s most differentiated and complete portfolio of content, brands and franchises across television, film, sports, news, streaming and gaming.",
        'hiring_needs': 'Production Assistant, for a TV production set in Los Angeles in June 2025',
        'specific_benefits': 'Weekly Pay, Employee Meals, healthcare',
    }

    crew = JobPostingCrew().crew()

    # Run AI agents
    result = crew.kickoff(inputs=inputs)

    # Extract values for database
    company = inputs['company_domain']
    role = inputs['hiring_needs']

    # Save result to Supabase
    save_job(company, role, str(result))

    # Print output
    print("\n✅ Job Posting Generated:\n")
    print(result)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company_domain': 'careers.wbd.com',
        'company_description': "Warner Bros. Discovery is a premier global media and entertainment company...",
        'hiring_needs': 'Production Assistant, for a TV production set in Los Angeles in June 2025',
        'specific_benefits': 'Weekly Pay, Employee Meals, healthcare',
    }

    try:
        JobPostingCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")