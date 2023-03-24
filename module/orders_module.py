from distutils.log import debug
from email import message
from http.client import responses
from telnetlib import STATUS
from urllib import response
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from db.database import *
from model.orders_model import *
from crud.orders_crud import *
from fastapi.security.api_key import APIKey
import auth
from html_response_codes import *

router = APIRouter(dependencies=[Depends(auth.get_api_key)])


@router.get("/",responses = {200:ExampleResponseModel(data=[orders_out_model.Config.schema_extra['example']],message='User Found'),404:ExampleErrorResponseModel(404, 'Not Found'),400:ExampleErrorResponseModel(400, "Bad Request")})
async def get_all_orders(db: Session = Depends(get_db)):
    response = await get_all(db)
    return response

@router.get("/{order_id}",responses = {200:ExampleResponseModel(data=[orders_out_model.Config.schema_extra['example']],message='User Found'),404:ExampleErrorResponseModel(404, 'Not Found'),400:ExampleErrorResponseModel(400, "Bad Request")})
async def get_order(order_id: int,db: Session = Depends(get_db)):
    response = await get(db,id=order_id)
    return response

@router.post('/',responses = {200:ExampleResponseModel(data=[orders_out_model.Config.schema_extra['example']],message='User Found'),201:ExampleResponseModel(data='...',message='New User Created'),404:ExampleErrorResponseModel(404, 'Not Found'),400:ExampleErrorResponseModel(400, "Bad Request")})
async def add_order(order_data:orders_in_model,db: Session = Depends(get_db)):
    response = await post(db,payload=order_data)
    return response

# @router.put('/',responses = {200:ExampleResponseModel(data=[orders_out_model.Config.schema_extra['example']],message='User Found'),404:ExampleErrorResponseModel(404, 'Not Found'),400:ExampleErrorResponseModel(400, "Bad Request")})
# async def delete_user(user_id:int,db: Session = Depends(get_db)):
#     response = await put(id=user_id)
#     return response
