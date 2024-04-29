import pytest

from lab1_cli import Lab1API


def dir_from_file(file_path, delimiter: str):
    return delimiter.join(file_path.split(delimiter)[:-1])


d = "\\"
FIXTURE_DIR_PATH = f'{dir_from_file(__file__, d)}/input_format_fixtures'


@pytest.mark.parametrize("file_with_test", [f"{FIXTURE_DIR_PATH}/01_empty_n_input.txt"])
def test_empty_input(file_with_test):
    return_code = Lab1API.write_in_console_from_file("python3 main.py", file_with_test)
    assert return_code == 0
