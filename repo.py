from sqlalchemy.ext.asyncio import AsyncSession
from models import ProductCreate
from orm_models import Product


class ProductRepo:
    async def create_product(self, db: AsyncSession, product:ProductCreate)-> Product:
        new_product = Product(product_code=Product.product_code,product_name = Product.product_name,unit_price = Product.unit_price,
                              available_quantity=Product.available_quantity,active=Product.is_active,category_id=Product.category_id)
        db.add(product)
        await db.flush()
        return new_product
