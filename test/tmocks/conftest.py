import pytest

from src.api import User


@pytest.fixture
def fixture_get_user_adi() -> User:
    return User(id=0, name="Adi")
