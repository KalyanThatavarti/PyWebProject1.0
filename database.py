from sqlalchemy import create_engine, text
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()
user = os.getenv("USER")


# user is defined in .env file as database connection string. make sure user id, password and database are secret and
# should not me checked in to gethub

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
