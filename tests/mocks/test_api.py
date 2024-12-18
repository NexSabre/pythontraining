from src.api import get_user, User


def test_get_user_from_api(mocker) -> None:
    """Mocking"""
    mocker.patch("src.api.NAME", "Jordan")
    assert get_user().name == "Jordan"


def test_get_user_and_check_it_can_fly(mocker) -> None:
    user: User = User(id=0, name="Jordan")
    assert not user.can_fly(), "User should not be able to fly"

    mocker.patch.object(user, "can_fly", return_value=True, autospec=True)
    assert user.can_fly(), "User is able to fly"


def test_get_user_refresh_data_and_check(mocker) -> None:
    user: User = User(id=0, name="Jordan")

    spy = mocker.spy(user, "refresh")

    for _ in range(2):
        user.refresh()
    else:
        assert spy.call_count == 2, "Refresh should be called twice"
        assert spy.spy_return is None, "Refresh should not return anything"
