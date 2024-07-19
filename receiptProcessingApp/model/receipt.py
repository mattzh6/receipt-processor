from typing import List
from pydantic import BaseModel, Field
from receiptProcessingApp.model.item import Item

class Receipt(BaseModel):
    retailer: str = Field(pattern=r"^[\w\s&-]+$")
    purchase_date: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$", alias="purchaseDate")
    purchase_time: str = Field(pattern=r"^\d{2}:\d{2}$", alias="purchaseTime")
    items: List[Item] = Field(min_length=1)
    total: str = Field(pattern=r"^\d+\.\d{2}$")
