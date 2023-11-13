"""
Конфигурация базы данных для SQLAlchemy

FILE: db/config.py
"""
from sqlalchemy import create_engine


ECHO_DB = False
SQLALCHEMY_DATABASE_URL = f"sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=ECHO_DB, connect_args={"check_same_thread": False}
)
