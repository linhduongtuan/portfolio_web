# database/database.py
from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv
import os
import sys

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
print(f"DATABASE_URL: {DATABASE_URL}")  # Debug print

if not DATABASE_URL:
    print(
        "Error: DATABASE_URL is not set. Please check your .env file.", file=sys.stderr
    )
    sys.exit(1)

engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
