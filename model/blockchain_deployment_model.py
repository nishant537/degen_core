from pydantic import BaseModel
from typing import Optional

class blockchain_deployment_model(BaseModel):
    blockchain_id: int
    deployment_id: int
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "blockchain_id": "2",
                "deployment_id": "1",
            }
        }

class blockchain_deployment_out_model(BaseModel):
    id: int
    blockchain_id: int
    deployment_id: int
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "1",
                "blockchain_id": "2",
                "deployment_id": "1",
            }
        }


