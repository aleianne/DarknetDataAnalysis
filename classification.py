import pandas as pd
import numpy as np


class Classification:
    """ this class is in charge to load and classify the tuple passed as argument """

    def __init__(self):

        ''' the classification logic is the following:
        
                SDC-1: the top ranked element predicted by the DNN is different from that predicted by its fault-free execution. 
                This is the most critical SDC because the top ranked element is what is typically used for downstream processing
                
                SDC-10%: the confidence score of the top ranked element varies by more than +/-10% of its fault-free execution 
                
                SDC-20%: the confidence score of the top ranked element varies by more than +/-20% of its fault-free execution
                
        '''

        # cp means correct prediction, bp means bad prediction, wp means wrong prediction
        columns = pd.MultiIndex.from_product([['stuck-at-0', 'stuck-at-1'], ['SDC-1', 'SDC-10', 'SDC-20']])
        index = [23, 24, 25, 26, 27, 28, 29, 30]

        self.sdc_data_frame = pd.DataFrame(np.zeros((8, 6), dtype=int), index=index, columns=columns)

        # define a second data frame that contains all the wrong predicted label, differentiated for each single bit
        columns = np.arange(0, 10)
        index = np.arange(23, 31)

        self.corrupted_labels_df = pd.DataFrame(np.zeros((8, 10), dtype=int), index=index, columns=columns)

    def classify_data_frame(self, res_df, correct_label, correct_cs):
        fault_type = ""
        faulty_label = 0
        bit = 0
        margin = 0.0
        confidence_score = 0.0

        # iterate the entire data frame
        for i in res_df.index:
            faulty_label = res_df.loc[i, 'label']
            fault_type = res_df.loc[i, 'fault type']
            margin = res_df.loc[i, 'margin']
            confidence_score = res_df.loc[i, 'confidence score']
            bit = res_df.loc[i, 'bit']

            if faulty_label != correct_label:

                self.update_sdc_data_frame(bit, fault_type, 'SDC-1')
                self.update_corrupted_labels_data_frame(bit, faulty_label)

            else:

                # generate the confidence score margin
                upper_bound_20, lower_bound_20, upper_bound_10, lower_bound_10 = self.compute_confidence_score_margin(correct_cs)

                # check if the confidence score is between a given interval
                if confidence_score > upper_bound_10 or confidence_score < lower_bound_10:
                    self.update_sdc_data_frame(bit, fault_type, 'SDC-10')

                if confidence_score > upper_bound_20 or confidence_score < lower_bound_20:
                    self.update_sdc_data_frame(bit, fault_type, 'SDC-20')

    def compute_confidence_score_margin(self, correct_cs):
        # define the bound for the correct classification
        upper_bound_20 = correct_cs + 0.2
        upper_bound_10 = correct_cs + 0.1
        lower_bound_20 = correct_cs - 0.2
        lower_bound_10 = correct_cs - 0.1

        if upper_bound_20 > 1.0:
            upper_bound_20 = 1.0

        if lower_bound_20 < 0.0:
            lower_bound_20 = 0.0

        if upper_bound_10 > 1.0:
            upper_bound_10 = 1.0

        if lower_bound_20 < 0.0:
            lower_bound_20 = 0.0

        return upper_bound_20, lower_bound_20, upper_bound_10, lower_bound_10

    def update_sdc_data_frame(self, bit, fault_type, sdc_type):
        """ this method should update the data frame in order to store the fault information"""

        # check if the label are between the range of 0 and 10
        if bit < 23 or bit > 30:
            print("impossible to store the information into the correct bit")
            raise Exception

        p_value = self.sdc_data_frame.loc[bit, (fault_type, sdc_type)]
        p_value += 1
        self.sdc_data_frame.at[bit, (fault_type, sdc_type)] = p_value

    def update_corrupted_labels_data_frame(self, bit, label):
        """ this method update the wrong label data frame """

        if bit < 23 or bit > 30:
            print("impossible to store the information into the correct bit")
            raise Exception

        if label < 0 or label > 9:
            print("impossible to store the information into the correct label")
            raise Exception

        # update a the wrong label prediction data frame
        p_value = self.corrupted_labels_df.loc[bit, label]
        p_value += 1
        self.corrupted_labels_df.at[bit, label] = p_value

    def get_wrong_df(self):
        return self.corrupted_labels_df

    def get_classification_df(self):
        return self.sdc_data_frame
