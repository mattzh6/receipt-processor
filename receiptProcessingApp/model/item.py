from pydantic import BaseModel, Field

class Item(BaseModel):
    short_description: str = Field(pattern=r"^[\w\s&-]+$", alias="shortDescription")
    price: str = Field(pattern=r"^\d+\.\d{2}$")
