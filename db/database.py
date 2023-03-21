from ast import For, Str
from datetime import datetime
from email.policy import default
from locale import currency
import string
from tkinter import CASCADE
from unicodedata import category
from xmlrpc.client import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, MetaData, Enum, DateTime, Float,create_engine, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from databases import Database
from fastapi import HTTPException,status
# from html_response_codes import *
import enum


DATABASE_URL= "sqlite:////C:/Users/nisha/Desktop/degen_money/sql_app.db"
APITOKEN="bzARDatkDXorjXpd3yiwhz6LAcpAnrGy3agckFpR"

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class StatusEnum(enum.Enum):
    live = 'Live'
    alpha = "Alpha"
    beta = "Beta"

class User(Base):
    __tablename__ = "user"

    id = Column(Integer,primary_key = True,index = True)
    firstname = Column(String(45), nullable = False)
    lastname = Column(String(45), nullable = False)
    username = Column(String(45), nullable = False, unique=True)
    email = Column(String(45), nullable = False, unique=True)
    password = Column(String(45), nullable = False)
    last_login = Column(TIMESTAMP, default = datetime.now())
    created_at = Column(TIMESTAMP)


class OrderTypeEnum(enum.Enum):
    live = "BUY"
    beta = "SELL"
class Order(Base):
    __tablename__ = "order"

    id = Column(Integer,primary_key = True,index = True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    type = Column(Enum(OrderTypeEnum))
    symbol = Column(String(64), nullable = False)
    status = Column(String(64))
    updated_at = Column(TIMESTAMP, default = datetime.now())
    created_at = Column(TIMESTAMP)

class Orderbook(Base):
    __tablename__ = "orderbook"

    id = Column(Integer,primary_key = True,index = True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable = False)
    type = Column(Enum(OrderTypeEnum))
    symbol = Column(String(64), nullable = False)
    updated_at = Column(TIMESTAMP, default = datetime.now())
