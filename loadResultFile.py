import pandas as pd


class LoadResultFile:
    """ this class should be used in order to load a new file into to a pandas dataframe """

    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load_new_data_frame(self):

        if self.df is None:

            # load the information stored into the file into a new data frame
            self.df = pd.read_csv(self.filepath, sep="\t")

        return self.df








