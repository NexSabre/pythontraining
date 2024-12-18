import os

def test_mock_dict(mocker) -> None:
    environ_values = os.environ
    assert environ_values.get("KEY") is None
    mocker.patch.dict("os.environ", {"KEY": "VALUE1234567890"})

    assert os.environ.get("KEY") == "VALUE1234567890"