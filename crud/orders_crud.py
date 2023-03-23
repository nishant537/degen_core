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

'''
Add User
'''
async def post(db: Session,payload: orders_in_model):
    data = db.query(Order).filter(payload.name == Order.name).first()
    if data == None or len(data) == 0:
        data = Order(name=payload.name,description=payload.description)
        db.add(data)
        db.commit()
        db.refresh(data)
    return data


'''
Get Protocol
'''
async def get(db: Session, id: int):
    data = db.query(Protocol).filter(Protocol.id == id).first()
    return data

'''
Fetch all Protocols
'''
async def get_all(db: Session):
    data = db.query(Protocol).all()
    return data

