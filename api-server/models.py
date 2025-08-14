from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# ================================================================
# Purpose of this file (models.py)
#
# Defines the SQLAlchemy ORM model representing the "messages" table
# in the SQLite database.
#
# SQLAlchemy ORM allows us to interact with the database using
# Python classes and objects instead of raw SQL queries.
#
# This model maps to the "messages" table with the following columns:
# - id (Integer, primary key, auto-incremented)
# - content (String, required)
#
# This structure is used by SQLAlchemy to:
# - Create tables automatically
# - Insert, query, update, delete rows easily using Python code
# ================================================================

# Create a base class for the ORM models
Base = declarative_base()

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# ================================================================
# Purpose of this file (models.py)
#
# Defines the SQLAlchemy ORM model representing the "messages" table
# in the SQLite database.
#
# SQLAlchemy ORM allows us to interact with the database using
# Python classes and objects instead of raw SQL queries.
# ================================================================

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)  # YYYY-MM-DD
    time = Column(String)
    place = Column(String)
    note = Column(String)

# Define the Message model, representing a message record in the database
class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    order = Column(Integer, nullable=False)  # NEW: Order position

