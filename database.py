from sqlalchemy import create_engine, text
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()
user = os.getenv("USER")

# user is defined in .env file as database connection string. make sure user id, password and database are secret and
# should not be checked in to gethub

engine = create_engine(
    user,
    echo=True)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        column_names = result.keys()
        jobs = []
        for row in result.all():
            jobs.append(dict(zip(column_names, row)))
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {'val': id})
        row = result.fetchone()
        return row._asdict()


def add_application_to_db(job_id, data):
    with engine.connect() as conn:

        values = {'job_id': job_id,
                  'first_name': data['First_name'],
                  'last_name': data['Last_name'],
                  'email': data['email'],
                  'mobile': data['mobile'],
                  'education': data['education'],
                  'work_experience': data['work_experience'],
                  'resume_url': data['resume_url']
                  }
        query = text(
            "INSERT INTO applications(job_id, first_name, last_name, email, mobile, education, work_experience, resume_url) VALUES (:job_id, :first_name, :last_name, :email, :mobile, :education, :work_experience, :resume_url)")

        values = {'job_id': job_id,
                  'first_name': data['First_name'],
                  'last_name': data['Last_name'],
                  'email': data['email'],
                  'mobile': data['mobile'],
                  'education': data['education'],
                  'work_experience': data['work_experience'],
                  'resume_url': data['resume_url']
                  }

        conn.execute(query, values)
        conn.commit()