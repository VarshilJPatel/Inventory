from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.sql import func

from src.core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    sku = Column(String(50), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(1000))

    price = Column(Numeric(10, 2), nullable=False)
    quantity_in_stock = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )