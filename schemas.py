from pydantic import BaseModel
# Event schemas for calendar app
class EventBase(BaseModel):
    date: str
    time: str
    place: str
    note: str

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    pass

class EventOut(EventBase):
    id: int
    class Config:
        orm_mode = True
from pydantic import BaseModel

# ================================================================
# Purpose of this file (schemas.py)
#
# Defines the expected structure of data for creating or updating
# messages in the API using Pydantic models.
#
# Pydantic's BaseModel automatically:
# - Validates incoming data (type checking, required fields)
# - Parses incoming JSON into structured Python objects
# - Generates automatic OpenAPI (Swagger) documentation
# - Provides 422 error responses if validation fails
#
# Example:
#  - Frontend sends JSON: { "content": "Hello World" }
#  - FastAPI automatically parses it into: MessageCreate(content="Hello World")
#
# If the frontend sends wrong data like { "text": "wrong" },
# FastAPI will automatically reject it with a 422 error (Unprocessable Entity).

# ================================================================



# Schema representing the structure of a message for creation and update operations
# Schema representing the structure of a message for creation and update operations
class MessageCreate(BaseModel):
    content: str

# 🆕 Schema for updating message order (used for reordering multiple messages)
class MessageOrderUpdate(BaseModel):
    id: int
    order: int
