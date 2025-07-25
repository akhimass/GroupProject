# schemas/ingredient.py
from pydantic import BaseModel

class IngredientBase(BaseModel):
    name: str
    quantity: int

class IngredientCreate(IngredientBase):
    pass

class Ingredient(IngredientBase):
    id: int

    class Config:
        orm_mode = True