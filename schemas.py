from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    
    class Config:
        from_attributes = True  # Замена orm_mode = True для Pydantic v2

class TransactionCreate(BaseModel):
    amount: float
    description: str
    category: str
    date: datetime
    type: str  # "income" или "expense"

class TransactionResponse(TransactionCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True
        