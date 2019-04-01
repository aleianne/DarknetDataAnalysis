from pathlib import Path


class LoadFile:

    def __init__(self, filename):

        if isinstance(filename, Path):
            self.filename = filename
        elif isinstance(filename, str):
            self.filename = Path(filename)
        else:
            raise Exception("the type of object path ins not known")

    def check_file(self):

        if self.filename.exists() and self.filename.is_file():
            return True
        else: 
            return False
