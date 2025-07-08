from pydantic import BaseModel
from typing import Optional
import enum

class OrderStatus(str, enum.Enum):
    PENDING = "Pending"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"

class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    image_url: Optional[str] = None
    stock: int = 0
    category_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    category: Category

    class Config:
        orm_mode = True

class Order(BaseModel):
    id: int
    user_id: int
    status: OrderStatus
    total: float

    class Config:
        orm_mode = True
