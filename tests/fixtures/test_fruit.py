import pytest

from src.fruit import Fruit, FruitSalad


@pytest.fixture
def get_apple() -> Fruit:
    """
    Create a simple fixture.
    :return a Fruit object called apple
    """
    return Fruit(name="apple")


@pytest.fixture
def list_ingredients(get_apple) -> list[Fruit]:
    """
    Create simple case of fixture which reuse another one.
    :param get_apple: return an object of the Fruit - apple
    :return: a list of the ingredients required for the fruit salad
    """
    return FruitSalad(ingredients=[get_apple, Fruit(name="banana")]).ingredients


def test_make_salad(list_ingredients) -> None:
    """
    In this case we reuse booth fixtures and checking that ingredients were
    correctly created.
    """
    assert len(list_ingredients) == 2, "Len of the list should be equal to 2"
