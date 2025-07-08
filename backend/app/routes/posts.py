from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

class Post(BaseModel):
    id: int
    user_id: int
    content: str

router = APIRouter()

fake_posts_db = [Post(id=1, user_id=1, content="Hello Uni-One!")]

@router.get("/", response_model=List[Post])
async def list_posts():
    return fake_posts_db
