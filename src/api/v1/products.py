from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.repositories.product_repository import ProductRepository
from src.schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductUpdate
)

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)

@router.post(
    "",
    response_model=ProductResponse,
    status_code=201,
)
def create_product(
    payload: ProductCreate,
    db: Session = Depends(get_db),
):
    return ProductRepository.create(
        db=db,
        product_data=payload,
    )

@router.get(
    "",
    response_model=list[ProductResponse],
    status_code=200,
)
def list_products(
    db: Session = Depends(get_db),
):
    return ProductRepository.list(
        db=db,
    )

@router.get(
    "/{id}",
    response_model=ProductResponse,
    status_code=200,
)
def get_product(
    id: int,
    db: Session = Depends(get_db),
):
    product = ProductRepository.get(
        db=db,
        product_id=id,
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return product

@router.delete(
    "/{id}",
    status_code=204,
)
def delete_product(
    id: int,
    db: Session = Depends(get_db),
):
    deleted = ProductRepository.delete(
        db=db,
        product_id=id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return None

@router.put(
    "/{id}",
    response_model=ProductResponse,
    status_code=200,
)
def update_product(
    id: int,
    payload: ProductUpdate,
    db: Session = Depends(get_db),
):
    product = ProductRepository.update(
        db=db,
        product_id=id,
        product_data=payload
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return product