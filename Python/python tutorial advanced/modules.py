from contextlib import contextmanager
import os

@contextmanager
def change_dir(directory):
    try:
        cwd = os.getcwd()
        os.chdir(directory)
        yield
    finally:
        os.chdir(cwd)

