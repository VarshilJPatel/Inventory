from pydantic import BaseModel, EmailStr
from datetime import datetime

class CustomerCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    address: str | None = None

class CustomerUpdate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    address: str | None = None

class CustomerResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: str | None
    address: str | None
    created_at: datetime

    model_config = {
        "from_attributes": True
    }