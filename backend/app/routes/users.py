from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    name: str
    country: str

router = APIRouter()

fake_users_db = [User(id=1, name="Alice", country="Gambia")]

@router.get("/", response_model=List[User])
async def list_users():
    return fake_users_db
