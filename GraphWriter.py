import matplotlib.pyplot as plt


class GraphWriter:
    """ this class is in charge to design all the graph """

    def __init__(self, classification_df, wrong_df):
        self.classification_df = classification_df
        self.wrong_label_df = wrong_df

        # create a new figure that should contains all the axes
        self.figure = plt.figure()

    def create_new_graphics(self):
        # create two sub graph
        graphic_1 = self.figure.add_subplot(311)
        graphic_2 = self.figure.add_subplot(312)
        graphic_3 = self.figure.add_subplot(313)

        graphic_1.set_xlabel('bit')
        graphic_1.set_ylabel('classification')

        graphic_2.set_xlabel('bit')
        graphic_2.set_ylabel('classification')

        graphic_3.set_xlabel('bit')
        graphic_3.set_ylabel('label')

        # split the classification data frame into two sub data frame: one for stuck-at 1 and one for stuck-at 0
        sa1_df = self.classification_df['stuck-at-1']
        sa0_df = self.classification_df['stuck-at-0']

    def show_figures(self):
        self.figure.show()
