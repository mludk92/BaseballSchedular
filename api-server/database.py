from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# ================================================================
# Purpose of this file (database.py)
#
# Sets up the database connection and session management using SQLAlchemy.
#
# Key responsibilities:
# - Create a connection to a local SQLite3 database (messages.db)
# - Provide a reusable session object for interacting with the database
# - Initialize the database schema based on ORM models
#
# ================================================================

# Database connection URL (using SQLite, local file-based database)
#set relative path to the database file
DATABASE_URL = "sqlite:///./messages.db"

# Create the SQLAlchemy database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Required for SQLite threading behavior
)

# Create a configured "Session" class for database sessions
SessionLocal = sessionmaker(
    autocommit=False,     # Don't auto-commit transactions
    autoflush=False,      # Don't auto-flush before commit
    bind=engine           # Connect session to our engine
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
