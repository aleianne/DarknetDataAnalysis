from loadFile import LoadFile
from classification import Classification


class AnalyzeResFile(LoadFile):

    # this file should contains all the result that should be computed during the analysis phase
    def __init__(self, store_res, threshold):
        super(AnalyzeResFile, self).__init__()
        self.store_res = store_res
        self.classificator = Classification(threshold)

    def analyzeResFile(self, sa_data_frame, filename):
        
        # create two different data frame staring from the argument passed as parameter
        sa1_data_frame = sa_data_frame.loc[sa_data_frame['fault type'] == 'stuck-at-1']
        sa0_data_frame = sa_data_frame.loc[sa_data_frame['fault type'] == 'stuck-at-0']

        # retrieve from the storage the information about the golden prediction
        golden_pred_df = self.store_res.getGoldenPredictionDataFrame()
       
        # da controllare se il filename contiene l'estensione del file
        golden_label = golden_pred_df.loc[filename, 'label']

        # filter the correct data frame
        correct_sa1_df = sa1_data_frame[sa1_data_frame['label'] == golden_label]
        correct_sa0_df = sa0_data_frame[sa0_data_frame['label'] == golden_label]

        # filter the wrong data frame
        wrong_sa1_df = sa1_data_frame[sa1_data_frame['label'] != golden_label]
        wrong_sa0_df = sa0_data_frame[sa0_data_frame['label'] != golden_label]

        # group by the bit position the data frame in order to compute the frequency
        correct_sa1_df = correct_sa1_df.groupby('bit').size()
        correct_sa0_df = correct_sa0_df.groupby('bit').size()

        wrong_sa1_df = wrong_sa1_df.groupby('bit').size()
        wrong_sa0_df = wrong_sa0_df.groupby('bit').size()

        

    
        

