from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models.database import engine
from .models import models
from .routes import products, categories, orders, auth
from .utils.seed import seed_db

app = FastAPI(title="GlowCare Gambia API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def startup_event():
    from .models.database import SessionLocal
    db = SessionLocal()
    seed_db(db)
    db.close()

app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(categories.router, prefix="/categories", tags=["categories"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"message": "Welcome to GlowCare Gambia"}
