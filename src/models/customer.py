from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from src.core.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    full_name = Column(String(200), nullable=False)

    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20), nullable=False)

    address = Column(String(500))

    created_at = Column(DateTime(timezone=True), server_default=func.now())