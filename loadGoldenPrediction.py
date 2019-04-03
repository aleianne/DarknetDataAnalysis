from loadFile import LoadFile
from utils.utilFunction import del_ext_suffix

import pandas as pd


class LoadGoldenPrediction(LoadFile):
    """ this class should load the golden prediction file into a new data frame """

    def __init__(self, filename):
        super(LoadGoldenPrediction, self).__init__(filename)
        self.gold_pred_df = None
    
    def load_data_frame(self, skiprow=0):
        """ this method load the data frame from the file name specified into the constructor """

        if super(LoadGoldenPrediction, self).check_file():
            print("the file exists")
        else:
            # if is not possible to find the golden prediction exceptions throw a new FileNotFoundError
            raise FileNotFoundError

        # check if should be skipped some row
        if skiprow == 0:
            self.gold_pred_df = pd.read_csv(self.filename, sep='\t')
        else:
            self.gold_pred_df = pd.read_csv(self.filename, skiprows=[skiprow], sep='\t')

        # rename the image name column
        self.gold_pred_df['image name'] = self.gold_pred_df['image name'].map(del_ext_suffix)

        # set the image name as the index of the data frame in order to speed up the image retrieval
        self.gold_pred_df = self.gold_pred_df.set_index('image name')

    def print_golden_prediction_df(self):
        print(self.gold_pred_df)

    def get_gold_pred_data_frame(self):
        return self.gold_pred_df
