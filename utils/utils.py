import os


def get_mod_path():
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)

    return dir_path
