import os


def del_ext_suffix(name):
    """ delete the filename extension """

    filename = name
    ext = "init"

    while len(ext) != 0:
        filename, ext = os.path.splitext(ext)

    return filename
