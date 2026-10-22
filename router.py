import router
from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from models import ProductResponse, ProductCreate
from service import ProductService

router= APIRouter(prefix="/products",tags=["Products"])
vehicle_service=ProductService()

@router.post("",response_model=ProductResponse,status_code=201)
async def create_product(product:ProductCreate,db:AsyncSession=Depends(get_session)) -> ProductResponse:
    return await ProductService.create_product(db,product)

