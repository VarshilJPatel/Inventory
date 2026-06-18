from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field


class OrderCreate(BaseModel):
    customer_id: int
    product_id: int
    quantity: int = Field(default=1, gt=0)


class OrderUpdate(BaseModel):
    quantity: int = Field(gt=0)
    status: str


class OrderResponse(BaseModel):
    id: int
    customer_id: int
    product_id: int
    quantity: int
    total_amount: Decimal
    unit_price: Decimal
    status: str
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {
        "from_attributes": True
    }