from sqlalchemy.orm import Session
from auth import get_password_hash, verify_password
from models import User, Transactions
from schemas import UserCreate, TransactionCreate
from datetime import datetime

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_transactions_by_user_id(db: Session, user_id: int):
    return db.query(Transactions).filter(Transactions.user_id == user_id)

def add_transactions(db: Session, user_id: int, transaction: TransactionCreate):
    db_transaction = Transactions(
        amount=transaction.amount,
        description=transaction.description,
        category=transaction.category,
        type=transaction.type,
        date=transaction.date,
        user_id=user_id
    )

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
