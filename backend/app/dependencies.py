from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from app.database import SessionLocal
from app.models import User  # Додайте цей імпорт для використання моделі User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_user(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
