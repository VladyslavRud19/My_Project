from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import User, UserCreate
from app.crud import create_user, get_user_by_username
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=User)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.get("/users/{username}", response_model=User)
def read_user(username: str, db: Session = Depends(get_db)):
    return get_user_by_username(db=db, username=username)
