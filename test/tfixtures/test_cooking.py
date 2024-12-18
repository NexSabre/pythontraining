import pytest

from src.cooking import set_owen, start_owen, stop_owen


@pytest.fixture
def start_and_stop_owen() -> None:
    """
    This fixture include finalizer.
    """
    start_owen()  # This is Set up
    yield None  # Optionally you can return setup results
    stop_owen()  # This is teardown, this part of the code will be run
    #  after all.


def test_check_owen_set_temperature_correctly(start_and_stop_owen: None) -> None:
    assert set_owen(30) == 30, "Owen should be set to 30"


def test_check_owen_set_temperature_without_fixture() -> None:
    start_owen()

    assert set_owen(30) == 30, "Owen should be set to 30"

    stop_owen()
