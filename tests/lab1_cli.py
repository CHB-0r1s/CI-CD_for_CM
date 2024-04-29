from subprocess import Popen, PIPE
import shlex


def dir_from_file(file_path, delimiter: str):
    return delimiter.join(file_path.split(delimiter)[:-1])


class Lab1API:
    CWD_WIN_BORIS = "C:\\Users\\Борис\\PycharmProjects\\CI-CD_for_CM\\tests\\"
    CWD_PIPELINE = dir_from_file(__file__, "/")

    @staticmethod
    def write_in_console_from_file(command, file_path: str) -> int:
        print(file_path)
        file_with_input = open(file_path, "rb")
        command_and_param: list[str] = shlex.split(command, comments=False, posix=True)
        echo_command: list[str] = ["echo", file_with_input.read().replace(b"\r", b""), "|"]

        with Popen(echo_command + command_and_param, stdout=PIPE, stderr=PIPE, cwd=Lab1API.CWD_PIPELINE) as proc:
            return proc.wait()