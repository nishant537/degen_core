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

'''
Add Deployment
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
Get Deployment
'''
async def get(db: Session, id: int):
    data = db.query(Orderbook).filter(Orderbook.id == id).first()
    return data


'''
Fetch all Deployments
'''
async def get_all(db: Session):
    data = db.query(Orderbook).all()
    return data

