from classification import Classification


import pandas as pd


class AnalyzeResultFile:
    """
        this class should analyze the result file stored into the file system
    """

    def __init__(self, gold_prediction_df, threshold):
        # pass as argument to this class the golden prediction data frame
        self.gold_prediction_df = gold_prediction_df
        # create a new classification instance
        self.classification = Classification(threshold)

    def analyze_res_file(self, sa_data_frame, filename):
        # create two different data frame staring from the argument passed as parameter
        sa1_data_frame = sa_data_frame.loc[sa_data_frame['fault type'] == 'stuck-at-1']
        sa0_data_frame = sa_data_frame.loc[sa_data_frame['fault type'] == 'stuck-at-0']

        golden_label = self.gold_prediction_df.loc[filename, 'label']

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

        self.classification.update_classification()


class LoadResultFile(LoadFile):
    """ this class should load the single result file and analyze it """

    def __init__(self, filename, path):
        super(LoadResultFile, self).__init__(filename, path)
        self.res_data_frame = None

    def create_new_result_data_frame(self):

        # check if the file exists
        if not self.check_file():
            raise FileNotFoundError

        # if the file exists than load his data into a new data frame
        self.res_data_frame = pd.read_csv(self.filename, sep="\t")

        # return the data frame
        return self.res_data_frame

    def get_result_file_data_frame(self):
        return self.res_data_frame