from pathlib import Path


class MainDirectoryReader:

    def __init__(self, result_path):
        self.dirPath = None
        self.pathname = None
        self.file_list = None
        self.change_dir_path(result_path)

    def change_dir_path(self, result_path):
        
        if isinstance(result_path, Path):
            self.dirPath = result_path
            self.pathname = self.dirPath.as_posix()
        elif isinstance(result_path, str):
            self.dirPath = Path(result_path)
            self.pathname = result_path
        else:
            raise Exception("the object type that should be passed to the change_dir_path cab be string or Path")

    def create_file_list(self):
        ''' return the list of files contained into the directory specified by the path '''

        if not self.dirPath.exists() or not self.dirPath.is_dir():
            raise Exception("impossible to open the directory ", self.pathname)
        
        # create a list that contains the files contained into the directory
        # add into the list only the files and exclude the golden prediction file
        self.file_list = [x for x in self.dirPath.iterdir()]

    def get_file_list(self):
        if len(self.file_list) == 0:
            self.create_file_list()
        
        return self.file_list

