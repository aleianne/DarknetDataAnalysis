from loadFile import LoadFile
import pandas as pd

def image_renaming(name):
    splits = name.split('.')
    return splits[0]

class LoadGoldenPrediction(LoadFile):

    def __init__(self, filename, path):
        super(LoadGoldenPrediction, self).__init__(filename, path)
        self.goldPredDF = None
    
    def load_data_frame(self):
        exists = self.check_file_existence()

        if (exists == True):
            print("the file exists")
        else 
            print("the file doesn't exists")
            return 

        # load the new dataframe that contains the golden predictions
        filepath = self.filepath.as_posix()
        # load the golden prediction file
        self.goldPredDF = pd.read_csv(filepath, sep='\t')
        # rename the image name column
        self.goldPredDF['image name'] = self.goldPredDF['image name'].map(image_renaming)
        
    def get_gpred_dataframe(self):
        return self.goldPredDF


