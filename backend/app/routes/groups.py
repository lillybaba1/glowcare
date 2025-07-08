from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

class Group(BaseModel):
    id: int
    name: str
    description: str

router = APIRouter()

fake_groups_db = [Group(id=1, name="AfroTech", description="African tech enthusiasts")]

@router.get("/", response_model=List[Group])
async def list_groups():
    return fake_groups_db
