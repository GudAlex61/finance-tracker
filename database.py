from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Используем SQLite для простоты (можно заменить на PostgreSQL позже)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, 
        connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    # Создаем все таблицы
    Base.metadata.create_all(bind=engine)
    
    # Можно добавить начальные данные здесь, если нужно
    db = SessionLocal()
    try:
        # Пример: добавление начального пользователя
        from models import User
        from auth import get_password_hash
        
        # Проверяем, есть ли уже пользователи
        if not db.query(User).first():
            hashed_password = get_password_hash("adminpassword")
            admin_user = User(
                username="admin",
                email="admin@example.com",
                hashed_password=hashed_password
            )
            db.add(admin_user)
            db.commit()
            print("Создан начальный пользователь: admin/adminpassword")
    except Exception as e:
        print(f"Ошибка при инициализации БД: {e}")
    finally:
        db.close()