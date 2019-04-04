from os.path import expanduser, splitext
from pathlib import Path


def del_ext_suffix(name):
    """ delete the filename extension """

    filename = name
    ext = "init"

    while len(ext) != 0:
        filename, ext = splitext(filename)

    return filename


def generate_path1(filename, path):
    homepath = Path(expanduser('~'))
    filepath = homepath / path / filename
    return filepath


def generate_path2(path):
    homepath = Path(expanduser('~'))
    filepath = homepath / path
    return filepath

