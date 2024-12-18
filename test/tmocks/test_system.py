def test_mock_opening_files(mocker) -> None:
    """
    Mocking the open function.
    """
    mocker.patch("builtins.open", mocker.mock_open(read_data="data"))
    with open("file") as file:
        assert file.read() == "data"