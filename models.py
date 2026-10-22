from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict



class ProductCreate(BaseModel):
    product_code: str = Field(min_length=1, max_length=40)
    product_name: str = Field(min_length=1, max_length=150)
    unit_price: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    available_quantity: int = Field(ge=0)
    active: bool = True
    category_id: int

class ProductResponse(ProductCreate):
    product_id: int
    category_name: str


    model_config = ConfigDict(from_attributes=True)