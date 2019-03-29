from loadFile import LoadFile

import pandas as pd

# this function split the image name in order to extract the name from the
def image_renaming(name):
    splits = name.split('.')
    return splits[0]


class LoadGoldenPrediction(LoadFile):

    def __init__(self, filename, path):
        super(LoadGoldenPrediction, self).__init__(filename, path)
        self.gold_pred_df = None
    
    def load_data_frame(self):
        exists = super(LoadGoldenPrediction, self).check_file()

        if exists:
            print("the file exists")
        else:
            print("the file doesn't exists")
            return 

        # load the new data frame that contains the golden predictions
        filepath = self.filepath.as_posix()
        # load the golden prediction file
        self.gold_pred_df = pd.read_csv(filepath, sep='\t')
        # rename the image name column
        self.gold_pred_df['image name'] = self.gold_pred_df['image name'].map(image_renaming)
        # set the image name as the index of the data frame in order to speed up the image retrieval
        self.gold_pred_df = self.gold_pred_df.set_index('image name')

    def get_gpred_dataframe(self):
        return self.gold_pred_df


