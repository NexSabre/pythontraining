import pytest

from unittest.mock import patch
from pytest_mock import mocker
from src.api import get_user, User


def test_get_user_from_api(mocker) -> None:
    """Mocking"""
    mocker.patch("src.api.NAME", "Jordan")
    assert get_user().name == "Jordan"


# or
# using a decorator @mocker.patch 

@patch("src.api.NAME", "Jordan")
def test_get_user_from_api_using_mocker_decorator() ->  None:
    assert get_user().name == "Jordan"


def test_get_user_and_check_it_can_fly(mocker) -> None:
    user: User = User(id=0, name="Jordan")
    assert not user.can_fly(), "User should not be able to fly"

    mocker.patch.object(user, "can_fly", return_value=True, autospec=True)
    assert user.can_fly(), "User is able to fly"


@patch("src.api.User.refresh", side_effect=Exception("timeout"))
def test_get_user_and_check_it_can_fly_using_decorator(refresh, fixture_get_user_adi) -> None:
    """
    This test will faile because the refresh method is raising an exception, 
    it's mocked to raise an exception, so the test will fail.
    """
    user = fixture_get_user_adi
    with pytest.raises(Exception) as error:
        user.refresh()
        assert error == "timeout"


def test_get_user_refresh_data_and_check(mocker) -> None:
    user: User = User(id=0, name="Jordan")

    spy = mocker.spy(user, "refresh")

    for _ in range(2):
        user.refresh()
    else:
        assert spy.call_count == 2, "Refresh should be called twice"
        assert spy.spy_return is None, "Refresh should not return anything"

@patch.object(User, "status")
def test_get_user_status(status) -> None:
    user: User = User(id=0, name="Jordan")
    status.return_value = "Jordan is NOT a user"
    assert user.status() == "Jordan is NOT a user"

    adi_user = User(id=1, name="Adi")
    assert adi_user.status() != "Adi is a user"
    # the effect is pername, so the status will be same for each user instance

    assert status.call_count == 2, "Status should be called twice"

def test_patch_user_status_with_context_manager(mocker) -> None:
    user: User = User(id=0, name="Jordan")
    with patch.object(user, "status", return_value="Jordan is NOT a user") as status:
        assert user.status() == "Jordan is NOT a user"
    assert status.call_count == 1, "Status should be called once"