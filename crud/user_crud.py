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
async def post(db: Session,payload: user_in_model):
    data = db.query(User).filter(payload.username == User.username).first()
    if data == None or len(data) == 0:
        data = User(firstname=payload.firstname,lastname=payload.lastname,username=payload.username,email=payload.email,password=payload.password,created_at = payload.created_at)
        db.add(data)
        db.commit()
        db.refresh(data)
        return ResponseModel(201,"New User Created")
    else:
        return ResponseModel(200,"Duplicate User Found")       


'''
Get User by username
'''
async def get(db: Session, username: str):
    query = db.query(User).filter(User.username==username)
    data = query.first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ErrorResponseModel(404, 'Not Found'))
    else:
        return ResponseModel(data = data, message = "User Found")  

'''
Fetch all Users
'''
async def get_all(db: Session):
    query = db.query(User)
    data = query.all()
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

