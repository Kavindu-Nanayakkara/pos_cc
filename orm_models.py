import datetime

from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Category(Base):
    __tablename__ = "category"

    category_id = Column(Integer,primary_key=True,index=True)
    category_code=Column(String,unique=True,nullable=False)
    category_name=Column(String,nullable=False)
    description = Column(String)
    is_active = Column(Boolean)

class Product(Base):
    __tablename__ = "product"

    product_id = Column(Integer,primary_key=True,index=True)
    product_code=Column(String,unique=True,nullable=False)
    product_name=Column(String,nullable=False)
    unit_price = Column(Numeric,nullable=False)
    available_quantity = Column(Integer,nullable=False)
    is_active = Column(Boolean)
    category_id = Column( Integer,ForeignKey("category.id"))

class Customer(Base):
    __tablename__="customer"

    customer_id = Column(Integer,primary_key=True,index=True)
    mobile_number = Column(String)
    full_name = Column(String,nullable=False)
    email = Column(String,unique=True,nullable=False)
    loyalty_points = Column(Numeric,nullable=False)
    registerd_at = Column(DateTime)

# class Order(Base):
#     __tablename__="order"
#
#     order_id = Column(Integer,primary_key=True,index=True)
#     customer_id = Column(Integer)
#     order_date = Column(DateTime)
#     order_status = Column(String,nullable=False)
#     total = Column(Numeric)
#     loyalty_points = Column(Integer)
#
#
# class OrderItem(Base):
#     __tablename__="order"
#
#     order_item_id = Column(Integer,primary_key=True,index=True)
#     order_id = Column(Integer)
#     product_id = Column(DateTime)
#     quantity = Column(String,nullable=False)
#     unit_price = Column(Numeric)
#     sub_total = Column(Numeric)









