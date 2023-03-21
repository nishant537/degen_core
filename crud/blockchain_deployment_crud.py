from json import JSONEncoder
import logging
import re
# from urllib import request
from sqlalchemy import select
from db.database import *
from model.blockchain_deployment_model import *
from sqlalchemy.orm import Session
from fastapi import Depends,Header,Request,status,HTTPException
from typing import Optional, Union

'''
Add BlockchainDeployment
'''
async def post(database: Session,payload: blockchain_deployment_model):
    query = BlockchainDeployment.select().where(payload.blockchain_id == BlockchainDeployment.c.blockchain_id,payload.deployment_id == BlockchainDeployment.c.deployment_id)
    data = await database.fetch_one(query=query)
    if data == None or len(data) == 0:
        query = BlockchainDeployment.insert().values(blockchain_id=payload.blockchain_id,deployment_id =payload.deployment_id )
        data = await database.execute(query=query)
        return ResponseModel(201,"New BlockchainDeployment Created")
    else:
        return ResponseModel(200,"Duplicate BlockchainDeployment Found")       


'''
Get BlockchainDeployment
'''
async def get(database: Session, id: int):
    query = BlockchainDeployment.select().where(BlockchainDeployment.c.id == id)
    data = await database.fetch_one(query=query)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ErrorResponseModel(404, 'Not Found'))
    else:
        return ResponseModel(data = data, message = "BlockchainDeployment Found")  


'''
Fetch all BlockchainProtocols
'''
async def get_all(database: Session):
    query = BlockchainDeployment.select()
    data = await database.fetch_all(query=query)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ErrorResponseModel(404, 'Not Found'))
    else:
        return ResponseModel(data = data, message = "BlockchainDeployment Found")   

