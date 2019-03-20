from loadFile import LoadFile
import pandas as pd

class LoadResultFile(LoadFile):

    def __init__(self, filename, path):
        super(LoadResultFile, self).__init__(filename, path)
        self.res_dataframe = None

    def create_new_result_dataframe(self):

        # check if the file exists
        if (self.check_file()):
            print("ok the file exists")
        else:
            raise: Exception("impossible to open the file because it doesn't exist")

        # load the new data frame using pandas
        # todo controllare se il file in input contiene l'header e a quale riga cominciano i dati
        # convert the file path to posix string
        filename = self.filepath.as_posix()
        self.res_dataframe = pd.read_csv(filename, header=1, sep='\t')
    
    def get_result_file_dataframe(self):
        return self.res_dataframe
