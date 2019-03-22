from loadFile import LoadFile
from classification import Classification

class AnalyzeResFile(LoadFile):

    # this file should contains all the result that should be computed during the analysis phase

    def __init__(self, storeRes, threshold):
        self.storeRes = storeRes
        self.classificator = Classification(threshold)

    def analyzeResFile(self, saDataFrame, filename).
        
        # create two different dataframe staring from the argument passed as parameter
        sa1DataFrame = saDataFrame.loc[sa1DataFrame['fault type'] == 'stuck-at-1']
        sa0DataFrame = sa0DataFrame.loc[sa0DataFrame['fault type'] == 'stuck-at-0']

        # retrieve from the storage the information about the golden prediction
        goldenPredDf = storeRes.getGoldenPredictionDataFrame()
       
        # da controllare se il filename contiene l'estensione del file
        golden_label = goldenPredDf.loc[filename, 'label']

        # filter the correct dataframe 
        correct-sa1-df = sa1DataFrame[sa1DataFrame['label'] == golden_label]
        correct-sa0-df = sa0DataFrame[sa0DataFrame['label'] == golden_label]

        # filter the wrong dataframe
        wrong-sa1-df = sa1DataFrame[sa1DataFrame['label'] != golden_label]
        wrong-sa0-df = sa0DataFrame[sa0DataFrame['label'] != golden_label]

        # group by the bit position the data frame in order to compute the frequency
        correct-sa1-df = correct-sa1-df.group('bit').size()
        correct-sa0-df = correct-sa0-df.group('bit').size()

        wrong-sa1-df = wrong-sa1-df.group('bit').size()
        wrong-sa0-df = wrong-sa0-df.group('bit').size()

        

    
        

