from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from models import ProductCreate, ProductResponse
from repo import ProductRepo


class ProductService:

    def __init__(self):
        self.repository = ProductRepo()

    async def create_product(self, db: AsyncSession, product:ProductCreate) -> ProductResponse:
        category = await self.repository.get_category(db, product.category_id)

        if not category or not category.active:
            raise HTTPException(
                status_code=400,
                detail="Invalid or inactive category"
            )

        existing = await self.repository.get_by_code(
            db, product.product_code
        )

        if existing:
            raise HTTPException(
                status_code=409,
                detail="Product code already exists"
            )

        new_product = await self.repository.create_product(
            db, product
        )
        await db.commit()
        await db.refresh(new_product)

        return new_product
