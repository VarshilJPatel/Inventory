from pydantic import BaseModel, EmailStr

class CustomerCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str | None = None
    address: str | None = None

class CustomerUpdate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str | None = None
    address: str | None = None

class CustomerResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: str | None
    address: str | None

    model_config = {
        "from_attributes": True
    }