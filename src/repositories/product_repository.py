from sqlalchemy.orm import Session
from src.utils.generate_sku_id import generate_sku_id
from src.models.product import Product
from src.schemas.product import ProductCreate, ProductUpdate

class ProductRepository:
    @staticmethod
    def create(
        db: Session,
        product_data: ProductCreate
    ) -> Product:
        sku_id = generate_sku_id()
    
        product = Product(
            sku=sku_id,
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            quantity_in_stock=product_data.quantity_in_stock,
        )

        db.add(product)
        db.commit()
        db.refresh(product)

        return product
    
    @staticmethod
    def list(
        db: Session,
    ) -> list[Product]:
        return db.query(Product).all()

    @staticmethod
    def get(
        db: Session,
        product_id: int
    ) -> Product | None:
        product = (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

        if not product:
            return None

        return product

    @staticmethod
    def delete(
        db: Session,
        product_id: int
    ) -> bool:
        product = (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

        if not product:
            return False

        db.delete(product)
        db.commit()

        return True

    @staticmethod
    def update(
        db: Session,
        product_id: int,
        product_data: ProductUpdate
    ) -> Product | None:
        product = (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

        if not product:
            return None

        product.name = product_data.name
        product.description = product_data.description
        product.price = product_data.price
        product.quantity_in_stock = product_data.quantity_in_stock

        db.commit()
        db.refresh(product)

        return product