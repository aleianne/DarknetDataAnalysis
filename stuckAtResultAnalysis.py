from classification import Classification
from utils.constant import MARGIN_THRESHOLD, WRONG_LABELS_FILENAME, CLASSIFICATION_FILENAME
from utils.utilFunction import del_ext_suffix
from loadDataFrame import LoadDataFrame
from pathlib import Path
from utils.utilFunction import generate_path2, generate_path1

import timeit
import random


class StuckAtResultAnalysis:

    def __init__(self, dir_list, golden_pred_df):
        self.dir_list = dir_list
        self.result_classificator = Classification(MARGIN_THRESHOLD)
        self.result_files = []

        # define a new instance attribute that should contains the golden prediction data frame
        self.golden_pred_df = golden_pred_df

    def load_files(self):

        ext = ".csv"

        # load all the files contained into the directories into a list
        for d in self.dir_list:
            # create a new path
            directory_path = generate_path2(d)
            file_list = None

            # check if the directory exists
            if directory_path.exists() and directory_path.is_dir():
                file_list = [file for file in directory_path.iterdir() if self._check_extension(file, ext)]
                # add the files contained into the directory into the result file list
                if len(file_list) != 0:
                    self.result_files.extend(file_list)
            else:
                print("impossible to load the directory: ", directory_path.as_posix())

    def debug(self):

        print("DEBUG---")
        print("begin to analyze the data")
        file = random.choice(self.result_files)

        start = timeit.timeit()

        # for each file contained into the list, load the data into a new data frame
        res_file = LoadDataFrame(file)
        res_file.load_new_data_frame()
        df = res_file.get_result_data_frame()

        # get the correct label
        correct_label = 5

        # get the correct confidence score
        correct_cs = 0.8

        # begin to classify the data frame retrieved from the result file
        self.result_classificator.classify_data_frame(df, correct_label, correct_cs)

        end = timeit.timeit()

        classification_df = self.result_classificator.get_classification_df()

        print("analyzed file ", file.as_posix())
        print("analysis terminated in ", end - start, " seconds")

        print(classification_df)

    def print_all_files(self, show=False):

        if show:
            for file in self.result_files:
                print("file: ", file.as_posix())

        print("number of files to be analyzed: ", len(self.result_files))

    def analyze_stuck_at_faults(self):

        start = timeit.timeit()

        print("begin to analyze result files")
        print("number of files to be analyzed: ", len(self.result_files))

        for file in self.result_files:
            # for each file contained into the list, load the data into a new data frame
            res_file = LoadDataFrame(file)
            res_file.load_new_data_frame()
            df = res_file.get_result_data_frame()

            # get the correct label
            correct_label = self._get_correct_label(file)

            # begin to classify the data frame retrieved from the result file
            self.result_classificator.classify_data_frame(df, correct_label)

        end = timeit.timeit()

        print("analysis terminated in ", end - start, " seconds")

    def save_data_frames_into_csv(self, outdir):
        # get the classification data frame
        classification_df = self.result_classificator.get_classification_df()
        wrong_label_df = self.result_classificator.get_wrong_df()

        if classification_df.empty:
            print("classification data frame is empty")
            return

        if wrong_label_df.empty:
            print("wrong labels data frame is empty")
            return

        # generate the filename
        file_path_classification = generate_path1(CLASSIFICATION_FILENAME, outdir)
        file_path_wrong_label = generate_path1(WRONG_LABELS_FILENAME, outdir)

        classification_df.to_csv(file_path_classification, sep='\t')
        wrong_label_df.to_csv(file_path_wrong_label, sep='\t')

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
        filepath = None

        if isinstance(file, Path):
            filepath = file
        elif isinstance(file, str):
            filepath = Path(file)

        f_name = filepath.stem

        # delete the extension from the filename
        image_name = del_ext_suffix(f_name)

        return self.golden_pred_df.loc[image_name, 'golden prediction']



