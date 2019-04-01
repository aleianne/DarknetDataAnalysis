from classification import Classification
from utils.constant import MARGIN_THRESHOLD
from loadResultFile import LoadResultFile
from pathlib import Path

from os.path import expanduser


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
                file_list = [file for file in directory_path.iterdir() if self.check_extenstion(file, ext)]
                # add the files contained into the directory into the result file list
                if len(file_list) != 0:
                    self.result_files.extend(file_list)
            else:
                print("impossible to load the directory: ", directory_path.as_posix())

    def check_extenstion(self, filename, extension):
        # check if the filename passed as argument is a Path instance
        if not isinstance(filename, Path):
            if isinstance(filename, str):
                filename = Path(filename)

        for s in filename.suffixes:
            if s == extension:
                return True

        return False

    def analyze_single_file(self):

        for file in self.result_files:
            # for each file contained into the list, load the data into a new data frame
            res_file = LoadResultFile(file)
            res_df = res_file.load_new_data_frame()




    def get_result_files(self):
        return self.result_files


