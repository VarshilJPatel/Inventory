from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.repositories.customer_repository import CustomerRepository
from src.schemas.customer import (
    CustomerCreate,
    CustomerResponse,
    CustomerUpdate
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)

@router.post(
    "",
    response_model=CustomerResponse,
    status_code=201,
)
def create_customer(
    payload: CustomerCreate,
    db: Session = Depends(get_db),
):
    return CustomerRepository.create(
        db=db,
        customer_data=payload,
    )

@router.get(
    "",
    response_model=list[CustomerResponse],
    status_code=200,
)
def list_customers(
    db: Session = Depends(get_db),
):
    return CustomerRepository.list(
        db=db,
    )

@router.get(
    "/{id}",
    response_model=CustomerResponse,
    status_code=200,
)
def get_customer(
    id: int,
    db: Session = Depends(get_db),
):
    customer = CustomerRepository.get(
        db=db,
        customer_id=id,
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )

    return customer

@router.delete(
    "/{id}",
    status_code=204,
)
def delete_customer(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = CustomerRepository.delete(
        db=db,
        customer_id=id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )

    return None

@router.put(
    "/{id}",
    response_model=CustomerResponse,
    status_code=200,
)
def update_customer(
    id: int,
    payload: CustomerUpdate,
    db: Session = Depends(get_db),
):
    customer = CustomerRepository.update(
        db=db,
        customer_id=id,
        customer_data=payload
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )

    return customer