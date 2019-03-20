from pathlib import Path

class MainDirectoryReader():

    def __init__(self, resultPath):
        self.dirPath = None
        self.pathname = None
        self.file_list = None
        change_dir_path(resultPath)

    def change_dir_path(self, resultPath):
        
        if (isinstance(resultPath, Path)):
            self.dirPath = resultPath
            self.pathname = self.dirPath.as_posix()
        elif (isinstance(resultPath, String)):
            self.dirPath = Path(resultPath)
            self.pathname = resultPath
        else:
            raise: Exception("the object type that should be passed to the change_dir_path cab be string or Path")

    def create_file_list(self):
        ''' return the list of files contained into the directory specified by the path '''

        if(not self.dirPath.exists() or not self.dirPath.is_dir()):
            raise: Exception("impossible to open the directory ",self.pathname)
        
        # create a list that contains the files contained into the directory
        # add into the list only the files and exclude the golden prediction file
        self.file_list = [x for x in self.dirPath.iterdir()]

    def get_file_list(self):
        if (len(self.file_list) == 0):
            create_file_list()
        
        return self.file_list
        
