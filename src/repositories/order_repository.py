from sqlalchemy.orm import Session, joinedload
from sqlalchemy import desc
from src.models.order import Order
from src.models.customer import Customer
from src.models.product import Product
from src.schemas.order import OrderCreate, OrderUpdate

class OrderRepository:
    @staticmethod
    def create(
        db: Session,
        order_data: OrderCreate
    ) -> Order | None:
        customer = (
            db.query(Customer)
            .filter(Customer.id == order_data.customer_id)
            .first()
        )
        if not customer:
            return None

        product = (
            db.query(Product)
            .filter(Product.id == order_data.product_id)
            .first()
        )
        if not product:
            return None

        order = Order(
            customer_id=order_data.customer_id,
            product_id=order_data.product_id,
            quantity=order_data.quantity,
            unit_price=product.price,
            status="pending",
        )
        db.add(order)
        db.commit()
        db.refresh(order)
        return (
            db.query(Order)
            .options(joinedload(Order.customer), joinedload(Order.product))  # ← eager load
            .filter(Order.id == order.id)
            .first()
        )

    @staticmethod
    def list(
        db: Session,
    ) -> list[Order]:
        return db.query(Order).options(joinedload(Order.customer), joinedload(Order.product)).order_by(desc(Order.created_at)).all()

    @staticmethod
    def get(
        db: Session,
        order_id: int
    ) -> Order | None:
        order = (
             db.query(Order)
            .options(joinedload(Order.customer), joinedload(Order.product))  # ← eager load
            .filter(Order.id == order_id)
            .first()
        )
        if not order:
            return None
        return order

    @staticmethod
    def delete(
        db: Session,
        order_id: int
    ) -> bool:
        order = (
            db.query(Order)
            .filter(Order.id == order_id)
            .first()
        )
        if not order:
            return False
        db.delete(order)
        db.commit()
        return True

    @staticmethod
    def update(
        db: Session,
        order_id: int,
        order_data: OrderUpdate
    ) -> Order | None:
        order = (
            db.query(Order)
            .filter(Order.id == order_id)
            .first()
        )
        if not order:
            return None
        order.quantity = order_data.quantity
        order.status = order_data.status
        db.commit()
        db.refresh(order)
        return (
            db.query(Order)
            .options(joinedload(Order.customer), joinedload(Order.product))  # ← eager load
            .filter(Order.id == order_id)
            .first()
        )