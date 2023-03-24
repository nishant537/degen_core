from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class user_in_model(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    username: str
    email: str
    password: str
    created_at : str
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "firstname": "Nishant",
                "lastname": "Goel",
                "username": "nishant537",
                "email": "nishantgoel.nishant@gmail.com",
                "password": "nishant537",
                "created_at": "datetime",
            }
        }

class user_out_model(BaseModel):
    id: int
    username: int
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
                "firstname": "Nishant",
                "lastname": "Goel",
                "username": "nishant537",
                "email": "nishantgoel.nishant@gmail.com",
                "password": "nishant537",
                "created_at": "datetime",
            }
        }


