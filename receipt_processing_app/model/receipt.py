from typing import List
from decimal import Decimal
from typing_extensions import Self
from pydantic import BaseModel, Field, model_validator, ValidationError
from receipt_processing_app.model.item import Item


class Receipt(BaseModel):
    retailer: str = Field(pattern=r"^[\w\s&-]+$")
    purchase_date: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$", alias="purchaseDate")
    purchase_time: str = Field(pattern=r"^\d{2}:\d{2}$", alias="purchaseTime")
    items: List[Item] = Field(min_length=1)
    total: str = Field(pattern=r"^\d+\.\d{2}$")

    @model_validator(mode="after")
    def check_total_price(self) -> Self:
        total_price = Decimal(self.total)
        prices_sum = 0
        for item in self.items:
            prices_sum += Decimal(item.price)

        if prices_sum != total_price:
            raise ValueError("the sum of the prices of the items must equal the total")
        return self
