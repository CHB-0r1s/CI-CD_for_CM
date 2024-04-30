from os import listdir, path

import pytest

from lab1_cli import Lab1API
from actions_manager import ActionsManager


def f_Antoha(a, b):
    return True


def dir_from_file(file_path, delimiter: str):
    return delimiter.join(file_path.split(delimiter)[:-1])


d = "/"
FIXTURE_DIR_PATH = f'{dir_from_file(__file__, d)}{d}input_fixtures'


def collect_tests_by_method(method: int):
    # https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    if method == 1:
        test_dir_path = FIXTURE_DIR_PATH + d + "G_Regular"
    elif method == 2:
        test_dir_path = FIXTURE_DIR_PATH + d + "Simple_Iter"
    else:
        print(method)
        raise Exception

    return [
        path.join(test_dir_path, f)
        for f in listdir(test_dir_path)
        if path.isfile(path.join(test_dir_path, f))
    ]


def test_workflow_init():
    assert ActionsManager.catch_required_method(), "Не удалось прочитать метод и stud-info.json"
    assert ActionsManager.catch_run_config(), "Не удалось прочитать конфиг из run.sh"


@pytest.mark.parametrize("test_file_path, ", collect_tests_by_method(ActionsManager.required_method))
def test_empty_input(test_file_path):
    run_command = ActionsManager.run_configuration
    return_code, meta_inf = Lab1API.write_in_console_from_file(run_command, test_file_path)
    assert f_Antoha(meta_inf, test_file_path)
    assert return_code == 0
