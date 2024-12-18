import os

def test_mock_dict(mocker) -> None:
    """
    Mocking the os.environ dictionary.
    Use mocker.patch.dict to mock a dictionary.
    """
    environ_values = os.environ
    assert environ_values.get("KEY") is None
    mocker.patch.dict("os.environ", {"KEY": "VALUE1234567890"})

    assert os.environ.get("KEY") == "VALUE1234567890"