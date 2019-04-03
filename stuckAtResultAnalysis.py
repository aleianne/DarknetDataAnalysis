from classification import Classification
from utils.constant import MARGIN_THRESHOLD
from utils.utilFunction import del_ext_suffix
from loadResultFile import LoadResultFile
from pathlib import Path
from os.path import expanduser
from fIlenameGenerator import FilenameGenerator

import timeit
import random


class StuckAtResultAnalysis:

    def __init__(self, dir_list, golden_pred_df):
        self.dir_list = dir_list
        self.result_clf = Classification(MARGIN_THRESHOLD)
        self.result_files = []
        self.golden_pred_df = golden_pred_df

        # create a new home path
        home = expanduser("~")
        self.home_path = Path(home)

    def load_files(self):
        # load into a list all the files contained into the directory

        for d in self.dir_list:
            # create a new path
            directory_path = self.home_path / d
            file_list = None

            # define the extension
            ext = ".csv"

            # check if the directory exists
            if directory_path.exists() and directory_path.is_dir():
                file_list = [file for file in directory_path.iterdir() if self._check_extension(file, ext)]
                # add the files contained into the directory into the result file list
                if len(file_list) != 0:
                    self.result_files.extend(file_list)
            else:
                print("impossible to load the directory: ", directory_path.as_posix())

    def debug(self):

        print("begin to analyze the data")
        file = random.choice(self.result_files)

        start = timeit.timeit()

        # for each file contained into the list, load the data into a new data frame
        res_file = LoadResultFile(file)
        res_file.load_new_data_frame()
        df = res_file.get_result_data_frame()

        # get the correct label
        correct_label = 5

        # begin to classify the data frame retrieved from the result file
        self.result_clf.classify_data_frame(df, correct_label)

        end = timeit.timeit()

        classification_df = self.result_clf.get_classification_df()

        print("analyzed file ", file.as_posix())
        print("analysis terminated in ", end - start, " seconds")

        print(classification_df)

    def print_all_files(self):

        for file in self.result_files:
            print("file: ", file.as_posix())

    def analyze_single_file(self):

        start = timeit.timeit()

        for file in self.result_files:
            # for each file contained into the list, load the data into a new data frame
            res_file = LoadResultFile(file)
            res_file.load_new_data_frame()
            df = res_file.get_result_data_frame()

            # get the correct label
            correct_label = self._get_correct_label(file)

            # begin to classify the data frame retrieved from the result file
            self.result_clf.classify_data_frame(df, correct_label)

        end = timeit.timeit()

        print("analysis terminated in ", end - start, " seconds")

    def save_data_frames_into_csv(self, outdir):
        # get the classification data frame
        classification_df = self.result_clf.get_classification_df()
        wrong_label_df = self.result_clf.get_wrong_df()

        if classification_df.empty:
            print("classification data frame is empty")
            return

        if wrong_label_df.empty:
            print("wrong labels data frame is empty")
            return

        # generate the filename
        file_path_classification = FilenameGenerator('classification.csv', outdir)
        file_path_wrong_label = FilenameGenerator('wrong_label.csv', outdir)

        classification_df.to_csv(file_path_classification.get_filepath(), sep='\t')
        wrong_label_df.to_csv(file_path_wrong_label.get_filepath(), sep='\t')

    def get_result_file(self):
        return self.result_files

    def _check_extension(self, filename, extension):
        # check if the filename passed as argument is a Path instance
        if not isinstance(filename, Path):
            if isinstance(filename, str):
                filename = Path(filename)

        for s in filename.suffixes:
            if s == extension:
                return True

        return False

    def _get_correct_label(self, file):
        # check if the name is a Path instance or a simple string
        file_s = None
        if isinstance(file, Path):
            file_s = file.as_posix()
        else:
            file_s = file

        # delete the extension from the filename
        image_name = del_ext_suffix(file_s)

        return self.golden_pred_df.loc[image_name]



