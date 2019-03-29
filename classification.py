import pandas as pd
import numpy as np

from ex.exceptions import WrongFaultModelException

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

        # define the index to be used into the data frame
        df_index = ('correct_p', 'bad_p', 'wrong_p')
        df_columns = [23, 24, 25, 26, 27, 28, 29, 30]

        # create a new data frame that should be used to store the classification 1
        self.sa0_df = pd.DataFrame(np.zeros((3, 8), dtype=int), index=df_index, columns=df_columns)
        self.sa1_df = pd.DataFrame(np.zeros((3, 8), dtype=int), index=df_index, columns=df_columns)

    def update_classification(self, df_tuple, correct_label):

        # TODO probabilmente la variabile confidence score non servirà

        # decode the tuple passed as argument
        wrong_label = df_tuple['label']
        bit = df_tuple['bit']
        confidence_score = df_tuple['confidence score']
        margin = df_tuple['margin']
        fault_model = df_tuple['margin']

        if correct_label == wrong_label:

            if margin > self.threshold:
                self.update_single_tuple(fault_model, 'correct_p', bit)
            else:
                self.update_single_tuple(fault_model, 'bad_p', bit)

        else:
            self.update_single_tuple(fault_model, 'wrong_p', bit)

    def update_single_tuple(self, model_type, index, col):
        """ this method should update the frequency """

        df = self.get_classification_df(model_type)

        p_value = df.loc[index, col]
        p_value += 1
        df.set_value(index, col, p_value)

    def get_classification_df(self, model_type):
        """ return the correct data frame """

        if model_type == "stuck-at-1":
            return self.sa1_df
        elif model_type == "stuck-at-0":
            return self.sa0_df

        raise WrongFaultModelException
