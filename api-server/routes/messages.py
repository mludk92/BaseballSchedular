from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List  # 🆕 Needed for type hints
from database import SessionLocal, init_db
from models import Message
from schemas import MessageCreate, MessageOrderUpdate
from logger import add_log

# ================================================================
# This router handles all /messages/ API endpoints
# ================================================================

router = APIRouter(prefix="/messages", tags=["Messages"])

# Dependency to get a database session
def get_db():
    """
    Provides a SQLAlchemy session for each request.
    Ensures session is closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize the database (create tables if they don't exist)
init_db()

# ================================================================
# Routes
# ================================================================

@router.get("/")
def get_messages(db: Session = Depends(get_db)):
    """
    Fetch all messages ordered by their 'order' value.
    """
    return db.query(Message).order_by(Message.order).all()

@router.post("/")
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    """
    Create a new message with automatically assigned order.
    """
    max_order = db.query(func.max(Message.order)).scalar() or 0
    new_message = Message(content=message.content, order=max_order + 1)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    add_log(f"Message created: {new_message.content} with order {new_message.order}")
    return new_message

@router.post("/reorder")
def reorder_messages(order_updates: List[MessageOrderUpdate], db: Session = Depends(get_db)):
    """
    Reorder multiple messages by updating their 'order' fields.
    """
    for update in order_updates:
        message = db.query(Message).filter(Message.id == update.id).first()
        if message:
            message.order = update.order
    db.commit()
    return {"detail": "Order updated successfully"}

@router.put("/{message_id}")
def update_message(message_id: int, message: MessageCreate, db: Session = Depends(get_db)):
    """
    Update the content of an existing message.
    """
    existing_message = db.query(Message).filter(Message.id == message_id).first()
    if not existing_message:
        raise HTTPException(status_code=404, detail="Message not found")
    existing_message.content = message.content
    db.commit()
    db.refresh(existing_message)
    return existing_message

@router.delete("/{message_id}")
def delete_message(message_id: int, db: Session = Depends(get_db)):
    """
    Delete a message by ID.
    """
    message = db.query(Message).filter(Message.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    db.delete(message)
    add_log(f"Message deleted: {message.content} with order {message.order}")
    db.commit()
    return {"detail": "Message deleted"}
