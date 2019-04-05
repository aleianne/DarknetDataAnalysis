import pandas as pd

from utils.utilFunction import generate_path2


class LoadDataFrame:
    """ this class should be used in order to load a new file into to a pandas dataframe """

    def __init__(self, filepath):
        self.filepath = generate_path2(filepath)
        self.df = None

    def load_new_data_frame(self, skiprow=0):
        """ this method should read the input file and load the data """

        if self.df is None:

            if self.filepath.exists() and self.filepath.is_file():
                # check if should be skipped some row
                if skiprow == 0:
                    self.df = pd.read_csv(self.filepath, sep='\t')
                else:
                    self.df = pd.read_csv(self.filepath, skiprows=[skiprow], sep='\t')
            else:
                raise FileNotFoundError

    def get_result_data_frame(self):
        return self.df








