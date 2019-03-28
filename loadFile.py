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
        self.file_path = self.path / filename

    def check_file(self):

        if self.file_path.exists() and self.file_path.is_file():
            return True
        else: 
            return False
