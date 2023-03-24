from json import JSONEncoder
import logging
import re
# from urllib import request
from sqlalchemy import select
from db.database import *
from model.orders_model import *
from sqlalchemy.orm import Session
from fastapi import Depends,Header,Request,status,HTTPException
from typing import Optional, Union
from html_response_codes import *

'''
Add Order
'''
async def post(db: Session,payload: orders_in_model):
    data = db.query(Order).filter(payload.broker_id == Order.broker_id).first()
    if data == None or len(data) == 0:
        data = Order(name=payload.name,description=payload.description)
        db.add(data)
        db.commit()
        db.refresh(data)
        return ResponseModel(201,"New Order Created")
    else:
        return ResponseModel(200,"Duplicate Order Found")   


'''
Get Order
'''
async def get(db: Session, id: int):
    query = db.query(Order).filter(Order.id == id)
    data = query.all()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ErrorResponseModel(404, 'Not Found'))
    else:
        return ResponseModel(data = data, message = "Order Found")  

'''
Fetch all Orders
'''
async def get_all(db: Session):
    query = db.query(Order)
    data = query.all()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ErrorResponseModel(404, 'Not Found'))
    else:
        return ResponseModel(data = data, message = "Order Found")   

