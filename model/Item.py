from pydantic import BaseModel, Field

class Item(BaseModel):
    shortDescription: str = Field(pattern=r"^[\w\s&-]+$")
    price: str = Field(pattern=r"^\d+\.\d{2}$")

    @property
    def getShortDescription(self) -> str:
        return self.shortDescription

    @property
    def getPrice(self) -> str:
        return self.price