from pydantic import BaseModel
from typing import Optional

class protocol_model(BaseModel):
    name: str
    description: Optional[str] = None
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Full Validator",
                "description": "Contains entire history of blockchain",
            }
        }

class protocol_out_model(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "1",
                "name": "Full Validator",
                "description": "Contains entire history of blockchain",
            }
        }


