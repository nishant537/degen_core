from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class orderbook_in_model(BaseModel):
    user_id: int
    order_id: int
    type: str
    symbol: str
    status: str
    created_at : str
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "user_id": "int",
                "order_id": "int",
                "type": "str",
                "symbol": "str",
                "status": "str",
                "created_at ": "str"
            }
        }

class orderbook_out_model(BaseModel):
    id: int
    user_id: int
    order_id: int
    type: str
    symbol: str
    status: str
    updated_at: datetime
    created_at : datetime
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "int",
                "user_id": "int",
                "order_id": "int",
                "type": "str",
                "symbol": "str",
                "status": "str",
                "updated_at ": "str",
                "created_at ": "str"
            }
        }


