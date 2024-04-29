import pytest

from lab1_cli import Lab1API


def f_Antoha(a, b):
    return True


def dir_from_file(file_path, delimiter: str):
    return delimiter.join(file_path.split(delimiter)[:-1])


d = "/"
FIXTURE_DIR_PATH = f'{dir_from_file(__file__, d)}/input_fixtures'


@pytest.mark.parametrize("test_file_path, ", [f"{FIXTURE_DIR_PATH}/G_Regular/01_empty_n_input.txt"])
def test_empty_input(test_file_path):
    return_code, meta_inf = Lab1API.write_in_console_from_file("python3 main_si.py", test_file_path)
    assert f_Antoha(meta_inf, test_file_path)
    assert return_code == 0
