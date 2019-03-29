from loadFile import LoadFile

import pandas as pd
import os


def del_ext_suffix(name):
    """ delete the filename extension """

    filename = name
    ext = "init"

    while len(ext) != 0:
        filename, ext = os.path.splitext(ext)

    return filename


class LoadGoldenPrediction(LoadFile):

    def __init__(self, filename, path):
        super(LoadGoldenPrediction, self).__init__(filename, path)
        self.gold_pred_df = None
    
    def load_data_frame(self):
        """ this method load the data frame from the file name specified into the constructor """

        if super(LoadGoldenPrediction, self).check_file():
            print("the file exists")
        else:
            # if is not possible to find the golden prediction ex throw a new FileNotFoundError
            raise FileNotFoundError

        # load the new data frame that contains the golden predictions
        self.gold_pred_df = pd.read_csv(self.filepath, sep='\t')

        # rename the image name column
        self.gold_pred_df['image name'] = self.gold_pred_df['image name'].map(del_ext_suffix)

        # set the image name as the index of the data frame in order to speed up the image retrieval
        self.gold_pred_df = self.gold_pred_df.set_index('image name')

    def get_gpred_dataframe(self):
        return self.gold_pred_df


