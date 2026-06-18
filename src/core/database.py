from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from collections.abc import Generator

from src.core.config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

from collections.abc import Generator


def get_db() -> Generator:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()