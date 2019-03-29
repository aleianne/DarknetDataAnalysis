import pandas as pd
import numpy as np


class Classification:

    def __init__(self, threshold):
        self.threshold = threshold

        # define the index to be used into the data frame
        i = ('sa1-cp', 'sa0-cp', 'sa1-wp', 'sa0-wp')
        c = [23, 24, 25, 26, 27, 28, 29, 30]

        # create a new data frame that should be used to store the classification 1
        self.class_df = pd.DataFrame(np.zeros((4, 8), dtype=int), i, c)

    def update_classification(self, fault_model, bit_position, correct_label, wrong_label):

        if correct_label == wrong_label:
            if fault_model == "stuck-at-1":
                self.update_single_tuple('', bit_position)
            elif fault_model == "stuck-at-0":
                self.update_single_tuple('', bit_position)
            else: 
                print("unknown fault type")
        else:   
            if fault_model == "stuck-at-1":
                self.update_single_tuple('', bit_position)
            elif fault_model == "stuck-at-0":
                self.update_single_tuple('', bit_position)
            else:
                print("unknown fault type")

    def update_single_tuple(self, index, col):
        """ this method should update the frequency """
        p_value = self.class_df.loc[index, col]
        p_value += 1
        self.class_df.set_value(index, col, p_value)

    def get_classification_df(self):
        return self.class_df
