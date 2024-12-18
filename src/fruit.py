from pydantic import BaseModel, Field


class Fruit(BaseModel):
    name: str


class FruitSalad(BaseModel):
    ingredients: list[Fruit] = Field(default_factory=list)


def make_salad(salad_recipe: FruitSalad) -> bool:
    return len(salad_recipe.ingredients) > 0
