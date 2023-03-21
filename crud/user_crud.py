from json import JSONEncoder
import logging
import re
# from urllib import request
from sqlalchemy import select
from db.database import *
from model.user_model import *
from sqlalchemy.orm import Session
from fastapi import Depends,Header,Request,status,HTTPException
from typing import Optional, Union
from html_response_codes import *


'''
Add User
'''
async def post(payload: user_in_model):
    query = user.select().where(payload.email == user.c.email)
    data = await database.fetch_one(query=query)
    if data == None or len(data) == 0:
        query = user.insert().values(username=payload.username,whmcs_id=payload.whmcs_id,email=payload.email,firstname=payload.firstname,lastname=payload.lastname)
        data = await database.execute(query=query)
        return ResponseModel(201,"New User Created")
    else:
        return ResponseModel(200,"Duplicate User Found")       


'''
Get User by username
'''
async def get(username: str):
    query = user.select().where(user.c.username == username)
    data = await database.fetch_one(query=query)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ErrorResponseModel(404, 'Not Found'))
    else:
        return ResponseModel(data = data, message = "User Found")  

'''
Fetch all Users
'''
async def get_all():
    query = user.select()
    data = await database.fetch_all(query=query)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ErrorResponseModel(404, 'Not Found'))
    else:
        return ResponseModel(data = data, message = "User Found")   

'''
Delete user
'''
# async def put(id: int):
#     query = user.select().where(id == user.c.id)
#     data = database.fetch_one(query=query)
#     if not data:
#         return ResponseModel(200,"User does not exist")       
#     else:
#         query = user.update().where(id == user.c.id).values(status="not active")
#         await database.execute(query=query)
#         return ResponseModel(201,"User details updated")   

