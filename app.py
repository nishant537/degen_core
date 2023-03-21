from distutils.log import debug
from email import message
from telnetlib import STATUS
from turtle import update
import uvicorn
from fastapi import FastAPI, Depends,status
from typing import Union
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from starlette.responses import PlainTextResponse, RedirectResponse
from db.database import *
from module import user_module,orders_module,orderbook_module
import os
import time
import asyncio
from threading import Thread
from html_response_codes import *


app = FastAPI(title='Edgevana Core')


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Triggered on starting of handler
@app.on_event("startup")
async def startup():
    try:
        await database.connect()
    except:
        return ErrorResponseModel(500, "Internal Server Error")

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(user_module.router, prefix="/user", tags=["User Data"])
app.include_router(orders_module.router, prefix="/order", tags=["Orders Data"])
app.include_router(orderbook_module.router, prefix="/orderbook", tags=["Orderbook Data"])

# if __name__ == "__main__":
#     uvicorn.run("app:app", host=HOST, port=PORT)