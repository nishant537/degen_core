from json import JSONEncoder
import logging
import re
# from urllib import request
from sqlalchemy import select
from db.database import *
from model.blockchain_protocol_model import *
from sqlalchemy.orm import Session
from fastapi import Depends,Header,Request,status,HTTPException
from typing import Optional, Union

'''
Add BlockchainProtocol
'''
async def post(database: Session,payload: blockchain_protocol_model):
    query = BlockchainProtocol.select().where(payload.blockchain_id == BlockchainProtocol.c.blockchain_id,payload.protocol_id == BlockchainProtocol.c.protocol_id)
    data = await database.fetch_one(query=query)
    if data == None or len(data) == 0:
        query = BlockchainProtocol.insert().values(blockchain_id=payload.blockchain_id,protocol_id =payload.protocol_id )
        data = await database.execute(query=query)
        return ResponseModel(201,"New BlockchainProtocol Created")
    else:
        return ResponseModel(200,"Duplicate BlockchainProtocol Found")       


'''
Get BlockchainProtocol
'''
async def get(database: Session, id: int):
    query = BlockchainProtocol.select().where(BlockchainProtocol.c.id == id)
    data = await database.fetch_one(query=query)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ErrorResponseModel(404, 'Not Found'))
    else:
        return ResponseModel(data = data, message = "BlockchainProtocol Found")  


'''
Fetch all BlockchainProtocols
'''
async def get_all(database: Session):
    query = BlockchainProtocol.select()
    data = await database.fetch_all(query=query)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ErrorResponseModel(404, 'Not Found'))
    else:
        return ResponseModel(data = data, message = "BlockchainProtocol Found")   

