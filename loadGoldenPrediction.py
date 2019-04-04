from utils.utilFunction import del_ext_suffix
from loadDataFrame import LoadDataFrame

import pandas as pd


class LoadGoldenPrediction(LoadDataFrame):
    """ this class should load the golden prediction file into a new data frame """

    def __init__(self, filepath):
        super(LoadGoldenPrediction, self).__init__(filepath)
    
    def load_golden_prediction_df(self, skiprow=0):
        """ this method load the data frame from the file name specified into the constructor """

        self.load_new_data_frame(skiprow)

        # rename the image name column
        self.df['image name'] = self.df['image name'].map(del_ext_suffix)

        # set the image name as the index of the data frame in order to speed up the image retrieval
        self.df = self.df.set_index('image name')

        print("Golden prediction file load correctly")

    def print_golden_prediction_df(self):
        print(self.df)

    def get_gold_pred_data_frame(self):
        return self.get_result_data_frame()
