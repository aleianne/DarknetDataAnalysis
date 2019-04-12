import pandas as pd

from utils.utilFunction import generate_path2
from pathlib import Path


class LoadDataFrame:
    """ this class should be used in order to load a new file into to a pandas dataframe """

    def __init__(self, path):

        if isinstance(path, str):
            self.file_path = generate_path2(path)
        elif isinstance(path, Path):
            self.file_path = path
        else:
            raise Exception()

        self.df = None

    def load_new_data_frame(self, skiprow=0):
        """ this method should read the input file and load the data """

        if self.df is None:

            if self.file_path.exists() and self.file_path.is_file():
                # check if should be skipped some row
                if skiprow == 0:
                    self.df = pd.read_csv(self.file_path, sep='\t')
                else:
                    self.df = pd.read_csv(self.file_path, skiprows=[skiprow], sep='\t')
            else:
                raise FileNotFoundError

        return self.df

    def get_result_data_frame(self):
        return self.df








