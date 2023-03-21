# from ast import Str
# from datetime import datetime
# from locale import currency
# import string
# from sqlalchemy import Float, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import os
# from enum import unique
# from sqlalchemy import INTEGER, VARCHAR, Boolean, Column, ForeignKey, Integer, String, Table, MetaData
# from sqlalchemy.orm import relationship
# from databases import Database
# from fastapi import HTTPException,status
# from html_response_codes import *


# DATABASE_URL = os.environ.get("DATABASE_URL")
# TOKEN = os.environ.get("TOKEN")
# # DATABASE_URL= "mysql+pymysql://edgevana_core:dAnhr9rDVFjU6RcC@edgevana-core-dev.c8j8f2adl52w.us-east-1.rds.amazonaws.com/edgevana_core"
# # APITOKEN="bzARDatkDXorjXpd3yiwhz6LAcpAnrGy3agckFpR"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# database = Database(DATABASE_URL)
# conn = engine.connect()

# async def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     # except:
#         # raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorResponseModel(400, "Bad Request"))
#     finally:
#         db.close()

# metadata = MetaData()

# user = Table(
#     "user",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("whmcs_id", Integer),
#     Column("username", String),
#     Column("firstname", String),
#     Column("lastname", String),
#     Column("email", String),
# )

# role = Table(
#     "role",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("description", String),
# )

# perm = Table(
#     "perm",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
# )

# org = Table(
#     "org",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("owner", Integer),
# )

# role_perm = Table(
#     "role_perm",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("role_id", Integer),
#     Column("perm_id", Integer),
# )

# org_role = Table(
#     "org_role",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("org_id", Integer),
#     Column("role_id", Integer),
# )

# user_org_role = Table(
#     "user_org_role",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("user_id", Integer),
#     Column("org_role_id", Integer),
# )

# location = Table(
#     "location",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("continent", String),
#     Column("country", String),
#     Column("county", String),
#     Column("state", String),
#     Column("city", String),
#     Column("address", String),
#     Column("zip", Integer),
#     Column("description", String),
#     Column("lattitude", Float),
#     Column("longitude", Float),
# )

# site = Table(
#     "site",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("hv_code", String),
#     Column("location_id", Integer),
# )

# service = Table(
#     "service",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("client_id", Integer),
#     Column("client_email", String),
#     Column("deviceid", String),
#     Column("whmcsid", Integer),
#     Column("translated_name", String),
#     Column("translated_groupname", String),
#     Column("servername", String),
#     Column("domain", String),
#     Column("serverhostname", String),
#     Column("date", String),
#     Column("status", String),
#     Column("username", String),
#     Column("boot", String),
#     Column("whmcs_hash", String),
#     Column("hv_code", String),
#     Column("ip", String),
# )

# cost = Table(
#     "cost",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("name", String),
#     Column("value", Float),
#     Column("currency", Integer),
#     Column("period", Integer),
#     Column("interval", Float),
#     Column("tags", String),
# )

# service_cost = Table(
#     "service_cost",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("service_id", Integer),
#     Column("cost_id", Integer),
# )

# specification = Table(
#     "specification",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", VARCHAR(60)),
#     Column("property", VARCHAR(60)),
#     Column("value", VARCHAR(256)),
# )

# service_spec = Table(
#     "service_spec",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("service_id", Integer),
#     Column("spec_id", Integer),
# )

# service_site = Table(
#     "service_site",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("service_id", Integer),
#     Column("site_id", Integer),
# )

# svctype = Table(
#     "svctype",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", VARCHAR(60)),
#     Column("description", String),
# )

# currency = Table(
#     "currency",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("acronym", VARCHAR(10)),
#     Column("name", VARCHAR(60)),
#     Column("description", VARCHAR(45)),
# )

# site_servers = Table(
#     "site_servers",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("site_id", Integer),
#     Column("count", Integer),
# )

# subscription = Table(
#     "subscription",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("user_id", Integer),
#     Column("edgevana_service_id", Integer),
#     Column("invoice_id", Integer),
#     # Column("start_date", datetime),
#     # Column("end_date", datetime),
# )

# benchmark = Table(
#     "benchmark",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("service_id", Integer),
#     Column("hash", String),
#     Column("key", String),
#     Column("value", Integer),
#     # Column("datetime", datetime),
# )

# activity_log = Table(
#     "activity_log",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("user_id", Integer),
#     Column("edgevana_service_id", Integer),
#     Column("ip", String),
#     Column("agent", Integer),
#     # Column("datetime", datetime),
# )

# blockchain = Table(
#     "blockchain",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("icon", String),
#     Column("status", String),
#     Column("description", String),
#     Column("decentralisation_score", String),
#     Column("usd_price", Integer),
# )

# tag = Table(
#     "tag",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("tag", String),
# )

# blockchain_tag = Table(
#     "blockchain_tag",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("blockchain_id", Integer),
#     Column("tag_id", Integer),
# )

# protocol = Table(
#     "protocol",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("type", String),
#     Column("description", String),
# )

# blockchain_protocol = Table(
#     "blockchain_protocol",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("blockchain_id", Integer),
#     Column("protocol_id", Integer),
# )

# blockchain_protocol_service = Table(
#     "blockchain_protocol_service",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("blockchain_protocol_id", Integer),
#     Column("protocol_service_id", Integer),
# )




