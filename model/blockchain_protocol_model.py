from pydantic import BaseModel
from typing import Optional

class blockchain_protocol_model(BaseModel):
    blockchain_id: int
    protocol_id: int
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "blockchain_id": "2",
                "protocol_id": "1",
            }
        }

class blockchain_protocol_out_model(BaseModel):
    id: int
    blockchain_id: int
    protocol_id: int
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "1",
                "blockchain_id": "2",
                "protocol_id": "1",
            }
        }


