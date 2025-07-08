from fastapi import FastAPI
from .routes import users, posts, groups

app = FastAPI(title="Uni-One API")

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(groups.router, prefix="/groups", tags=["groups"])

@app.get("/")
async def root():
    return {"message": "Welcome to Uni-One"}
