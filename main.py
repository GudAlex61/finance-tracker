from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import secrets
from sqlalchemy.orm import Session
from database import get_db, engine, Base, init_db
from models import User, Transactions
from schemas import UserCreate, UserResponse, TransactionCreate, TransactionResponse
from crud import create_user, get_user_by_username, get_transactions_by_user_id, add_transactions
from auth import verify_password, get_password_hash
import logging
import sys

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# Инициализация базы данных при запуске
init_db()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBasic()

def get_current_user(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    logger.info(f"Authenticating user: {credentials.username}")
    
    user = get_user_by_username(db, credentials.username)
    if not user:
        logger.warning(f"User not found: {credentials.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    # Проверяем пароль
    if not verify_password(credentials.password, user.hashed_password):
        logger.warning(f"Invalid password for user: {credentials.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    logger.info(f"User authenticated: {credentials.username}")
    return user

# Уберите дублирующий /login эндпоинт или измените его
@app.post("/login", response_model=UserResponse)
def login_for_token(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    """Альтернативный login через Basic Auth"""
    return get_current_user(credentials, db)

@app.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    existing_email = db.query(User).filter(User.email == user.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return create_user(db, user)

@app.get("/users/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/transactions/")
def get_transactions(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Transactions).filter(Transactions.user_id == current_user.id).all()

@app.post("/transactions/", response_model=TransactionResponse)
def create_transaction(
    transaction: TransactionCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return add_transactions(db, current_user.id, transaction)

@app.delete("/transactions/{id}", status_code=status.HTTP_200_OK)
def delete_transaction_by_id(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    logger.info(f"User {current_user.id} attempting to delete transaction {id}")
    transaction = db.query(Transactions).filter(Transactions.id==id, Transactions.user_id==current_user.id).first()
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")
    try:
        db.delete(transaction)
        db.commit()
        return {"message": "Transaction deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error deleting the transaction: {str(e)}")

@app.get("/summary")
def get_summary(current_user: User = Depends(get_current_user)):
    # Ваша логика получения сводки
    pass

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в FastAPI сервер"}

@app.get("/health")
def health_check():
    return {"status": "ok", "database": "initialized"}