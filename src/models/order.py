from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Numeric,
    DateTime,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.core.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False,
    )

    total_amount = Column(Numeric(12, 2), nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    customer = relationship("Customer")