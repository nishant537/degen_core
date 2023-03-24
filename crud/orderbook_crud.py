from json import JSONEncoder
import logging
import re
# from urllib import request
from sqlalchemy import select
from db.database import *
from model.orderbook_model import *
from sqlalchemy.orm import Session
from fastapi import Depends,Header,Request,status,HTTPException
from typing import Optional, Union
from html_response_codes import *

'''
Add Order to orderbook
'''
async def post(db: Session,payload: orderbook_in_model):
    data = db.query(Orderbook).filter(payload.name == Orderbook.name).first()
    if data == None or len(data) == 0:
        data = Orderbook(name=payload.name,description=payload.description)
        db.add(data)
        db.commit()
        db.refresh(data)
    return data


'''
Get Order
'''
async def get(db: Session, id: int):
    query = db.query(Orderbook).filter(id = id)
    data = query.all()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ErrorResponseModel(404, 'Not Found'))
    else:
        return ResponseModel(data = data, message = "Order Found")  


'''
Fetch all Orders in orderbook
'''
async def get_all(db: Session):
    query = db.query(Orderbook)
    data = query.all()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ErrorResponseModel(404, 'Not Found'))
    else:
        return ResponseModel(data = data, message = "Order Found")   

