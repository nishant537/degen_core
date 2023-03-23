from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class orders_in_model(BaseModel):
    user_id = int
    type = str
    symbol = str
    status = str
    created_at = datetime
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "type" : "str",
                "symbol" : "str",
                "status" : "str",
                "updated_at" : "datetime",
                "created_at" : "datetime"
            }
        }

class orders_out_model(BaseModel):
    id = int,
    user_id = int
    type = str
    symbol = str
    status = str
    updated_at = datetime
    created_at = datetime
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "type" : "str",
                "symbol" : "str",
                "status" : "str",
                "updated_at" : "datetime",
                "created_at" : "datetime"
            }
        }


