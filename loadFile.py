from pathlib import Path


class LoadFile:

    def __init__(self, filename, path):

        if isinstance(path, Path):
            self.path = path
        elif isinstance(path, str):
            self.path = Path(path)
        else:
            raise Exception("the type of object path ins not known")

        self.filename = filename
        self.filepath = self.path / filename

    def check_file(self):

        if self.filepath.exists() and self.filepath.is_file():
            return True
        else: 
            return False
