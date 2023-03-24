import asyncio
import os
import subprocess
import sys


def run_python(path_to_python_file: str, args: list[str] = None, env: dict[str, str] = None):
    """
    Run Python code in a separate process.

    """
    # setup environment
    env = os.environ.copy()
    env["PYTHONPATH"] = os.pathsep.join(sys.path)
    env["PYTHONUNBUFFERED"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"

    # run the code
    subprocess.run(
        [sys.executable, path_to_python_file] + (args or []),
        env=env,
        check=True,
    )


def run_background(path_to_file):
    """
    Run Python code in a separate process.

    """
    # setup environment
    env = os.environ.copy()
    env["PYTHONPATH"] = os.pathsep.join(sys.path)
    env["PYTHONUNBUFFERED"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"

    # run the code
    subprocess.Popen(
        [sys.executable, path_to_file],
        env=env,
    )


if __name__ == "__main__":
    run_python("run.py")
