from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models.database import SessionLocal
from ..models import models
from ..schemas import schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Order])
def list_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()
