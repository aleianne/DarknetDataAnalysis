import pandas as pd 


class StoreResults:

    # should be stored the dataframe that contains all the information needed for the analysis

    def __init__(self, goldenPredictionDF):
        self.goldenPredictionDF = goldenPredictionDF

    def get_golden_prediction_data_frame(self):
        return self.goldenPredictionDF
