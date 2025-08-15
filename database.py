from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import os

# ================================================================
# Purpose of this file (database.py)
#
# Sets up the database connection and session management using SQLAlchemy.
#
# Key responsibilities:
# - Create a connection to a Postgres database (DATABASE_URL from env)
# - Provide a reusable session object for interacting with the database
# - Initialize the database schema based on ORM models
# ================================================================

# Database connection URL (using Heroku Postgres)
DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Create the SQLAlchemy database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class for database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Initialize the database schema
def init_db():
    """
    Create all database tables based on the models defined in models.py.
    If the tables already exist, this function does nothing.
    """
    Base.metadata.create_all(bind=engine)
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
