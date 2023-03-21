from pydantic import BaseModel
from typing import Optional, List

class BlockchainModel(BaseModel):
    name: str
    icon: str
    status: str
    description: str
    decentralization_score: int = 0
    sustainability_score: int = 40
    available: bool = True
    categories: List[int] = []

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Solana",
                "status": "LIVE",
                "description": "Blockchain",
                "decentralization_score": 40,
                "sustainability_score": 40,
                "available": True,
                "categories": [1,2,3],
                "icon": "https://edgevana.com/img/solana-globe.webp",
            }
        }

class StartingPriceModel(BaseModel):
    currency: str
    currency_icon: str
    value: float
    blockchain_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "currency": "USD",
                "currency_icon": "https://edgevana.com/img/solana-globe.webp",
                "value": 52.20,
                "blockchain_id": 1
            }
        }

class CategoryModel(BaseModel):
    name: str
    icon: str = None
    blockchains: List[int] = []

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "DEFI",
                "currency_icon": "https://edgevana.com/img/solana-globe.webp",
                "blockchains": [1,2,3],
            }
        }
