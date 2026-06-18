from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.repositories.order_repository import OrderRepository
from src.schemas.order import (
    OrderCreate,
    OrderResponse,
    OrderUpdate
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)

@router.post(
    "",
    response_model=OrderResponse,
    status_code=201,
)
def create_order(
    payload: OrderCreate,
    db: Session = Depends(get_db),
):
    return OrderRepository.create(
        db=db,
        order_data=payload,
    )

@router.get(
    "",
    response_model=list[OrderResponse],
    status_code=200,
)
def list_orders(
    db: Session = Depends(get_db),
):
    return OrderRepository.list(
        db=db,
    )

@router.get(
    "/{id}",
    response_model=OrderResponse,
    status_code=200,
)
def get_order(
    id: int,
    db: Session = Depends(get_db),
):
    order = OrderRepository.get(
        db=db,
        order_id=id,
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return order

@router.delete(
    "/{id}",
    status_code=204,
)
def delete_order(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = OrderRepository.delete(
        db=db,
        order_id=id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return None

@router.put(
    "/{id}",
    response_model=OrderResponse,
    status_code=200,
)
def update_order(
    id: int,
    payload: OrderUpdate,
    db: Session = Depends(get_db),
):
    order = OrderRepository.update(
        db=db,
        order_id=id,
        order_data=payload
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return order