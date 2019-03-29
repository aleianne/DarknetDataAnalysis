class StoreResults:

    # should be stored the data frame that contains all the information needed for the analysis

    def __init__(self, golden_pred_df):
        self.golden_pred_df = golden_pred_df

    def get_golden_prediction_data_frame(self):
        return self.golden_pred_df
