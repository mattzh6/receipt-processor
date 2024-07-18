from typing import List
from pydantic import BaseModel, Field
from model.Item import Item

class Receipt(BaseModel):
    retailer: str = Field(..., pattern=r"^[\w\s&-]+$")
    purchaseDate: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$")
    purchaseTime: str = Field(..., pattern=r"^\d{2}:\d{2}$")
    items: List[Item] = Field(min_length=1)
    total: str = Field(..., pattern=r"^\d+\.\d{2}$")

    @property
    def getRetailer(self) -> str:
        return self.retailer

    @property
    def getPurchaseDate(self):
        return self.purchaseDate

    @property
    def getPurchaseTime(self):
        return self.purchaseTime

    @property
    def getItems(self):
        return self.items

    @property
    def getTotal(self):
        return self.total