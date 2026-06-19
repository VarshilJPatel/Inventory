from sqlalchemy.orm import Session
from sqlalchemy import desc
from src.models.customer import Customer
from src.schemas.customer import (
    CustomerCreate,
    CustomerUpdate,
)


class CustomerRepository:
    @staticmethod
    def create(
        db: Session,
        customer_data: CustomerCreate,
    ) -> Customer:
        customer = Customer(
            full_name=customer_data.full_name,
            email=customer_data.email,
            phone=customer_data.phone,
            address=customer_data.address,
        )

        db.add(customer)
        db.commit()
        db.refresh(customer)

        return customer

    @staticmethod
    def list(
        db: Session,
    ) -> list[Customer]:
        return db.query(Customer).order_by(desc(Customer.created_at)).all()

    @staticmethod
    def get(
        db: Session,
        customer_id: int,
    ) -> Customer | None:
        return (
            db.query(Customer)
            .filter(Customer.id == customer_id)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        customer_id: int,
        customer_data: CustomerUpdate,
    ) -> Customer | None:
        customer = (
            db.query(Customer)
            .filter(Customer.id == customer_id)
            .first()
        )

        if not customer:
            return None

        customer.full_name = customer_data.full_name
        customer.email = customer_data.email
        customer.phone = customer_data.phone
        customer.address = customer_data.address

        db.commit()
        db.refresh(customer)

        return customer

    @staticmethod
    def delete(
        db: Session,
        customer_id: int,
    ) -> bool:
        customer = (
            db.query(Customer)
            .filter(Customer.id == customer_id)
            .first()
        )

        if not customer:
            return False

        db.delete(customer)
        db.commit()

        return True