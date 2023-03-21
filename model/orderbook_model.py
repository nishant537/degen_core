from pydantic import BaseModel
from typing import Optional

class orderbook_in_model(BaseModel):
    id: int
    user_id: int
    type: str
    symbol: str
    status: str
    last_login: str
    created_at : str
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "whmcs_id": 2,
                "username": "nishant537",
                "first_name": "Nishant",
                "last_name": "Goel",
                "email": "nishant.goel@edgevana.com",
                "avatar": "http://s3.amazonaws.com/edgevana_avatar_bucket/1.jpg",
            }
        }

class orderbook_out_model(BaseModel):
    id: int
    name: str
    description: str
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "1",
                "name": "Full Validator",
                "description": "Contains entire history of blockchain",
            }
        }


