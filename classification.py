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

        # cp means correct prediction, bp means bad prediction, wp means wrong prediction

        # define a new multindex for the columns
        columns = pd.MultiIndex.from_product([['stuck-at-0', 'stuck-at-1'], ['cp', 'bp', 'wp']])
        index = [23, 24, 25, 26, 27, 28, 29, 30]

        self.clf_df = pd.DataFrame(np.random.randn(8, 6), index=index, columns=columns)

    def update_classification_df(self, res_df, correct_label):
        fault_type = ""
        faulty_label = 0
        margin = 0.0
        bit = 0

        # iterate the entire dataset
        for i in res_df.index:
            faulty_label = res_df.loc[i, 'label']
            fault_type = res_df.loc[i, 'faulty type']
            margin = res_df.loc[i, 'margin']
            bit = res_df.loc[i, 'bit']

            if faulty_label == correct_label:

                if margin >= self.threshold:
                    self.update_single_tuple(fault_type, bit, "cp")
                else:
                    self.update_single_tuple(fault_type, bit, "bp")

            else:

                self.update_single_tuple(fault_type, bit, "wp")

    def update_single_tuple(self, fault_type, bit, clf_value):
        """ this method should update the frequency """

        p_value = self.clf_df.loc[bit, (fault_type, clf_value)]
        p_value += 1
        self.clf_df.at[bit, (fault_type, clf_value)] = p_value

    def get_classification_df(self):
        return self.clf
