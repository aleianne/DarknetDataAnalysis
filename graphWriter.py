from loadGraphicsDataFrame import LoadGraphicsDataFrame
from utils.utilFunction import generate_path1

import matplotlib.pyplot as plt


# import matplotlib.pyplot as plt
#
#
# # class GraphWriter:
# #     """ this class is in charge to design all the graph """
# #
# #     def __init__(self):
# #         # create an array of figure, each of them will contains the proper plot
# #         self.plot_figures = []
# #         self.data_frames = []
# #
# #     def load_new_data_frame_2(self, classification_filename, wrong_label_filename):
# #         # create a new classification data frame loader
# #         classficationGraphicsLoader = LoadGraphicsDataFrame(classification_filename)
# #         # create a new wrong label data frame loader
# #         wrongLabelGraphicsLoader = LoadGraphicsDataFrame(wrong_label_filename)
# #
# #         classficationGraphicsLoader.load_graphics_data_frame(0, [0, 1])
# #         wrongLabelGraphicsLoader.load_graphics_data_frame(0, [0])
# #
# #         # append loaded data frames into the data frames list
# #         self.data_frames.append(classficationGraphicsLoader.get_graphics_data_frame())
# #         self.data_frames.append(wrongLabelGraphicsLoader.get_graphics_data_frame())
# #
# #     def create_new_graphics(self):
# #         # create a new figure for each data frame stored into this class
# #
# #         if len(self.data_frames):
# #             print("the data frame list is empty")
# #             return
# #
# #         for data_frame in self.data_frames:
# #             # append into data frames list each figure
# #             fig = plt.figure()
# #
# #             # create a new subplot
# #             fig.add_subplot("111")
# #             self.plot_figures.append(fig)
# #
# #
# #         #
# #         # # check if the two data frame are specified
# #         # if self.classification_df is None or self.wrong_label_df:
# #         #     print("impossible to create new graphics because the data frame are not specified")
# #         #     return
# #         #
# #         # # create two sub graph
# #         # graphic_1 = self.figure.add_subplot(311)
# #         # graphic_2 = self.figure.add_subplot(312)
# #         # graphic_3 = self.figure.add_subplot(313)
# #         #
# #         # graphic_1.set_xlabel('bit')
# #         # graphic_1.set_ylabel('classification')
# #         #
# #         # graphic_2.set_xlabel('bit')
# #         # graphic_2.set_ylabel('classification')
# #         #
# #         # graphic_3.set_xlabel('bit')
# #         # graphic_3.set_ylabel('label')
# #         #
# #         # # split the classification data frame into two sub data frame: one for stuck-at 1 and one for stuck-at 0
# #         # sa1_df = self.classification_df['stuck-at-1']
# #         # sa0_df = self.classification_df['stuck-at-0']
# #         #
# #         # sa1_df.plot.bar(ax=graphic_1)
# #         # sa0_df.plot.bar(ax=graphic_2)
# #         #
# #         # self.wrong_label_df.plot.bar(ax=graphic_3)
# #
# #     def save_graphics(self):
# #         pass
#
#
# def create_classification_df_graphic(classification_df_filaname):
#     classificationGraphicLoader = LoadGraphicsDataFrame(classification_df_filaname)
#     classification_df = classificationGraphicLoader.load_graphics_data_frame(0, [0, 1])
#
#     # create a new plot for the classification data frame
#     fig1 = plt.figure()
#
#     ax1 = fig1.add_subplot("211")
#     ax2 = fig1.add_subplot("211")
#
#     ax1.set_xlabel("bit")
#     ax1.set_ylabel("classification")
#
#     ax2.set_xlabel("bit")
#     ax2.set_ylabel("classification")
#
#
#     pass
#
# def create_wrong_label_df_graphic():
#     pass


def create_classification_graphics(df_filename, dir):
    # load the classification data frame
    index = 0
    header = [0, 1]
    classificationDfLoader = LoadGraphicsDataFrame(df_filename)
    classification_df = classificationDfLoader.load_graphics_data_frame(index, header)

    # create a new figure
    fig1 = plt.figure()

    ax1 = fig1.add_subplot(211)
    ax2 = fig1.add_subplot(212)

    output_figure_name = "classification.png"

    filepath = generate_path1(dir, output_figure_name)

    fig1.savefig(filepath)
    fig1.show()

