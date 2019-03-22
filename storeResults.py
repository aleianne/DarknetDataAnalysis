import pandas as pd 

class StoreResults():

    # should be stored the dataframe that contains all the information needed for the analysis


    

    def __init__(self, goldenPredictionDF):
        self.goldenPredictionDF = goldenPredictionDF

    def getGoldenPredictionDataFrame(self):
        return self.goldenPredictionDF

    

