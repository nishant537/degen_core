from distutils.log import debug
from email import message
from http.client import responses
from telnetlib import STATUS
from urllib import response
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from db.database import *
from model.user_model import *
from crud.user_crud import *
from fastapi.security.api_key import APIKey
import auth
from html_response_codes import *

router = APIRouter(dependencies=[Depends(auth.get_api_key)])


@router.get("/",responses = {200:ExampleResponseModel(data=[user_out_model.Config.schema_extra['example']],message='User Found'),404:ExampleErrorResponseModel(404, 'Not Found'),400:ExampleErrorResponseModel(400, "Bad Request")})
async def get_all_user():
    response = await get_all()
    return response

@router.get("/{username}",responses = {200:ExampleResponseModel(data=[user_out_model.Config.schema_extra['example']],message='User Found'),404:ExampleErrorResponseModel(404, 'Not Found'),400:ExampleErrorResponseModel(400, "Bad Request")})
async def get_user(username: str,db: Session = Depends(get_db)):
    response = await get(username=username)
    return response

@router.post('/',responses = {200:ExampleResponseModel(data=[user_out_model.Config.schema_extra['example']],message='User Found'),201:ExampleResponseModel(data='...',message='New User Created'),404:ExampleErrorResponseModel(404, 'Not Found'),400:ExampleErrorResponseModel(400, "Bad Request")})
async def add_user(user_data:user_in_model,db: Session = Depends(get_db)):
    response = await post(payload=user_data)
    return response

@router.put('/',responses = {200:ExampleResponseModel(data=[user_out_model.Config.schema_extra['example']],message='User Found'),404:ExampleErrorResponseModel(404, 'Not Found'),400:ExampleErrorResponseModel(400, "Bad Request")})
async def delete_user(user_id:int,db: Session = Depends(get_db)):
    response = await put(id=user_id)
    return response
