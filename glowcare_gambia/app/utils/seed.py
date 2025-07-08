from sqlalchemy.orm import Session
from ..models import models

SAMPLE_PRODUCTS = [
    {"name": "CeraVe Moisturizing Cream", "description": "Hydrates and restores the skin barrier.", "price": 15.99, "image_url": "https://example.com/cerave-cream.jpg", "stock": 20},
    {"name": "CeraVe Hydrating Cleanser", "description": "Gentle facial cleanser for normal to dry skin.", "price": 12.99, "image_url": "https://example.com/cerave-cleanser.jpg", "stock": 25},
    {"name": "Nivea Sunscreen", "description": "SPF 50+ protection.", "price": 9.99, "image_url": "https://example.com/nivea-sunscreen.jpg", "stock": 30},
]

SAMPLE_CATEGORIES = [
    {"name": "Skincare", "description": "Lotions and cleansers"},
    {"name": "Electronics", "description": "Gadgets and accessories"},
]

def seed_db(db: Session):
    if not db.query(models.Category).first():
        for cat in SAMPLE_CATEGORIES:
            category = models.Category(**cat)
            db.add(category)
        db.commit()
    if not db.query(models.Product).first():
        skincare = db.query(models.Category).filter_by(name="Skincare").first()
        for prod in SAMPLE_PRODUCTS:
            prod["category_id"] = skincare.id
            product = models.Product(**prod)
            db.add(product)
        db.commit()
