from pydantic import BaseModel
from typing import Optional

class user_in_model(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    username: str
    email: str
    password: str
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "firstname": "Nishant",
                "lastname": "Goel",
                "username": "nishant537",
                "email": "nishant.goel@edgevana.com",
                "password": "nishant537",
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
                "whmcs_id": 2,
                "username": "nishant537",
                "first_name": "Nishant",
                "last_name": "Goel",
                "email": "nishant.goel@edgevana.com",
                "avatar": "http://s3.amazonaws.com/edgevana_avatar_bucket/1.jpg",
            }
        }


