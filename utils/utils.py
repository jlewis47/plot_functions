import os


def get_mod_path():
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)

    return dir_path

def is_iter(test):

    try:
        iter(test)
        return(True)
    except TypeError:
        return(False)

