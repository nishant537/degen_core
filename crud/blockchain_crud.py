from json import JSONEncoder
import logging
import re
from this import d
# from urllib import request
from sqlalchemy import select
from db.database import *
from model.blockchain_model import *
from sqlalchemy.orm import Session
from fastapi import Depends,Header,Request,status,HTTPException
from typing import Optional, Union
import json


async def create(db: Session, create_body, table):
    try:
        db_item = table(**create_body.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        return

async def create_blockchain_service(db: Session, create_body, table):
    try:
        db_object = db.query(Category).filter(Category.id.in_(create_body.categories)).all()
        create_body.categories = db_object

        db_item = table(**create_body.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
        
    except Exception as e:
        return

async def create_category_service(db: Session, create_body, table):
    try:
        db_object = db.query(Blockchain).filter(Blockchain.id.in_(create_body.blockchains)).all()
        create_body.blockchains = db_object

        db_item = table(**create_body.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
        
    except Exception as e:
        return
