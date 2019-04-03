from os.path import expanduser
from pathlib import Path


class FilenameGenerator:

    def __init__(self, filename, dir):
        home_path = Path(expanduser('~'))
        self.filepath = home_path / dir / filename

    def check_file_existence(self):
        if self.filepath.exists() and self.filepath.is_file()
            return True
        else:
            return False

    def get_filepath(self):
        return self.filepath
