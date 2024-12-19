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

def test_mock_dict_multiple_keys(mocker) -> None:
    """
    Mocking the os.environ dictionary with multiple keys.
    """
    environ_values = os.environ
    assert environ_values.get("KEY1") is None
    assert environ_values.get("KEY2") is None
    mocker.patch.dict("os.environ", {"KEY1": "VALUE1", "KEY2": "VALUE2"})

    assert os.environ.get("KEY1") == "VALUE1"
    assert os.environ.get("KEY2") == "VALUE2"

def test_mock_dict_restore(mocker) -> None:
    """
    Mocking the os.environ dictionary and restoring it.
    """
    original_value = os.environ.get("KEY")
    mocker.patch.dict("os.environ", {"KEY": "TEMP_VALUE"})

    assert os.environ.get("KEY") == "TEMP_VALUE"

    mocker.stopall()
    assert os.environ.get("KEY") == original_value

# Exercise for the training:
# 1. Create a new test function `test_mock_dict_remove_key` that mocks the os.environ dictionary,
#    adds a key-value pair, and then removes the key. Verify that the key is removed.
# 2. Create a new test function `test_mock_dict_update_key` that mocks the os.environ dictionary,
#    adds a key-value pair, updates the value of the key, and verifies the updated value.
# 3. Create a new test function `test_mock_dict_clear` that mocks the os.environ dictionary,
#    clears all key-value pairs, and verifies that the dictionary is empty.