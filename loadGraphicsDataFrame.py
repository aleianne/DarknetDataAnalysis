from utils.utilFunction import generate_path2

import pandas as pd


class LoadGraphicsDataFrame:

    def __init__(self, filename):
        self.filepath = generate_path2(filename)
        self.df = None

    def load_graphics_data_frame(self, index, header):

        if self.df is None:
            header_list = None

            # check if the header is a list or not
            if not isinstance(header, list):
                header_list = [header]
            else:
                header_list = header

            # load a new data from from memory
            self.df = pd.read_csv(self.filepath, sep="\t", index=index, index_col=header_list)

        return self.df

    def get_graphics_data_frame(self):
        return self.df
