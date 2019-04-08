from loadGraphicsDataFrame import LoadGraphicsDataFrame

import matplotlib.pyplot as plt


class GraphWriter:
    """ this class is in charge to design all the graph """

    def __init__(self, classification_df=None, wrong_df=None):
        self.classification_df = classification_df
        self.wrong_label_df = wrong_df

        # create a new figure that should contains all the axes
        self.figure = plt.figure()

    def load_new_data_frame(self, classification_df, wrong_label_df):
        self.classification_df = classification_df
        self.wrong_label_df = wrong_label_df

    def load_new_data_frame_2(self, classification_filename, wrong_label_filename):
        # create a new classification data frame loader
        classficationGraphicsLoader = LoadGraphicsDataFrame(classification_filename)
        # create a new wrong label data frame loader
        wrongLabelGraphicsLoader = LoadGraphicsDataFrame(wrong_label_filename)

        classficationGraphicsLoader.load_graphics_data_frame(0, [0, 1])
        wrongLabelGraphicsLoader.load_graphics_data_frame(0, [0])

        self.classification_df = classficationGraphicsLoader.get_graphics_data_frame()
        self.wrong_label_df = wrongLabelGraphicsLoader.get_graphics_data_frame()

    def create_new_graphics(self):

        # check if the two data frame are specified
        if self.classification_df is None or self.wrong_label_df:
            print("impossible to create new graphics because the data frame are not specified")
            return

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

        sa1_df.plot.bar(ax=graphic_1)
        sa0_df.plot.bar(ax=graphic_2)

        self.wrong_label_df.plot.bar(ax=graphic_3)

    def show_figures(self):
        self.figure.show()
