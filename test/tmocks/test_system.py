def test_mock_opening_files(mocker) -> None:
    """
    Mocking the open function.
    """
    mocker.patch("builtins.open", mocker.mock_open(read_data="data"))
    with open("file") as file:
        assert file.read() == "data"

def test_mock_opening_files_write(mocker) -> None:
    """
    Mocking the open function for writing.
    """
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)
    with open("file", "w") as file:
        file.write("new data")
    mock_file().write.assert_called_once_with("new data")

def test_mock_opening_files_append(mocker) -> None:
    """
    Mocking the open function for appending.
    """
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)
    with open("file", "a") as file:
        file.write("appended data")
    mock_file().write.assert_called_once_with("appended data")

def test_mock_opening_files_readline(mocker) -> None:
    """
    Mocking the open function for reading lines.
    """
    mocker.patch("builtins.open", mocker.mock_open(read_data="line1\nline2\n"))
    with open("file") as file:
        assert file.readline() == "line1\n"
        assert file.readline() == "line2\n"

# Exercise for the training:
# 1. Create a new test function `test_mock_opening_files_readlines` that mocks the open function,
#    reads multiple lines from the file, and verifies the content of each line.
# 2. Create a new test function `test_mock_opening_files_read_binary` that mocks the open function,
#    reads binary data from the file, and verifies the content.
# 3. Create a new test function `test_mock_opening_files_write_binary` that mocks the open function,
#    writes binary data to the file, and verifies the written content.
# 4. Create a new test function `test_mock_opening_files_exception` that mocks the open function,
#    raises an exception when trying to open the file, and verifies that the exception is raised.