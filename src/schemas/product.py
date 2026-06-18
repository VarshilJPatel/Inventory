from decimal import Decimal

from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: Decimal
    quantity_in_stock: int = 0


class ProductResponse(BaseModel):
    id: int
    sku: str
    name: str
    description: str | None
    price: Decimal
    quantity_in_stock: int

    model_config = {
        "from_attributes": True
    }

class ProductUpdate(BaseModel):
    name: str
    description: str | None = None
    price: Decimal
    quantity_in_stock: int