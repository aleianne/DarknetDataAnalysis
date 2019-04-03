from pathlib import Path
from os.path import expanduser


class LoadFile:

    def __init__(self, filename):

        home_path = Path(expanduser('~'))

        if isinstance(filename, str):
            self.filename = home_path / filename
        else:
            raise Exception("the type of object path ins not known")

    def check_file(self):

        if self.filename.exists() and self.filename.is_file():
            return True
        else: 
            return False
