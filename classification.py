import pandas as pd
import numpy as np


class Classification:
    """ this class is in charge to load and classify the tuple passed as argument """

    def __init__(self, threshold):
        self.threshold = threshold

        ''' 
            the classification logic is the following:
            
                1 - if the label is correct, i.e. the network understand the correct label, and the margin between 
                    the most predicted label and the second most predicted label is below a certain threshold.
                    
                2 - if the label is correct, i.e. the network understand the correct label, and the margin between 
                    the most predicted label and the second most predicted label is higher than a certain threshold.
                    
                3 - if the label is not correct.   
        '''

        ''' the classification logic is the following:
        
                SDC-1: the top ranked element predicted by the DNN is different from that predicted by its fault-free execution. 
                This is the most critical SDC because the top ranked elemen is what is typically used for downstream processing
                
                SDC-10%: the confidence score of the top ranked element varies by more than +/-10% of its fault-free execution 
                
                SDC-20%: the confidence score of the top ranked element varies by more than +/-20% of its fault-free execution
                
        '''

        # cp means correct prediction, bp means bad prediction, wp means wrong prediction
        columns = pd.MultiIndex.from_product([['stuck-at-0', 'stuck-at-1'], ['cp', 'bp', 'wp']])
        index = [23, 24, 25, 26, 27, 28, 29, 30]

        self.clf_df = pd.DataFrame(np.zeros((8, 6), dtype=int), index=index, columns=columns)

        # define a second data frame that contains all the wrong predicted label, differentiated for each single bit
        columns = np.arange(0, 10)
        index = np.arange(23, 31)

        self.wrong_labels = pd.DataFrame(np.zeros((8, 10), dtype=int), index=index, columns=columns)

    def classify_data_frame(self, res_df, correct_label):
        fault_type = ""
        faulty_label = 0
        margin = 0.0
        bit = 0

        # iterate the entire data frame
        for i in res_df.index:
            faulty_label = res_df.loc[i, 'label']
            fault_type = res_df.loc[i, 'fault type']
            margin = res_df.loc[i, 'margin']
            bit = res_df.loc[i, 'bit']

            if faulty_label == correct_label:

                if margin >= self.threshold:
                    self.update_single_tuple(fault_type, bit, "cp")
                else:
                    self.update_single_tuple(fault_type, bit, "bp")

            else:

                self.update_wrong_label_data_frame(bit, faulty_label)

                # update the classification data frame
                self.update_single_tuple(fault_type, bit, "wp")

    def update_single_tuple(self, fault_type, bit, clf_value):
        """ this method should update the frequency """

        # check if the label are between the range of 0 and 10
        if bit < 23 or bit > 30:
            print("impossible to store the information into the correct bit")
            raise Exception

        p_value = self.clf_df.loc[bit, (fault_type, clf_value)]
        p_value += 1
        self.clf_df.at[bit, (fault_type, clf_value)] = p_value

    def update_wrong_label_data_frame(self, bit, label):
        """ this method update the wrong label data frame """

        if bit < 23 or bit > 30:
            print("impossible to store the information into the correct bit")
            raise Exception

        if label < 0 or label > 9:
            print("impossible to store the information into the correct label")
            raise Exception

        # update a the wrong label prediction data frame
        p_value = self.wrong_labels.loc[bit, label]
        p_value += 1
        self.wrong_labels.at[bit, label] = p_value

    def get_wrong_df(self):
        return self.wrong_labels

    def get_classification_df(self):
        return self.clf_df
