from loadFile import LoadFile

class AnalyzeResFile(LoadFile):

    # this file should contains all the result that should be computed during the analysis phase

    def __init__(self, storeRes):
        self.storeRes = storeRes

    def analyzeResFile(self, saDataFrame, filename).
        
        # create two different dataframe staring from the argument passed as parameter
        sa1DataFrame = saDataFrame.loc[sa1DataFrame['fault type'] == 'stuck-at-1']
        sa0DataFrame = sa0DataFrame.loc[sa0DataFrame['fault type'] == 'stuck-at-0']

        # retrieve from the storage the information about the golden prediction
        goldenPredDf = storeRes.getGoldenPredictionDataFrame()
       
        # da controllare se il filename contiene l'estensione del file
        golden_label = goldenPredDf.loc[filename, 'label']



    
        

