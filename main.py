import pandas as pd
import argparse

from pathlib import Path
from os.path import expanduser
from mainDirReader import MainDirectoryReader
from loadGoldenPrediction import LoadGoldenPrediction


'''def create_new_plot():
        plt.plot([1, 2, 3], [9, 89, 10])
        plt.ylabel('y-axis')
        plt.xlabel('x-axis')
        plt.show() 
'''


def analyze_single_res_dir(file_list, store_res):
    """ pass as argument to this function the list of the file contained into a single directory """

    for single_file in file_list:
        analyze_single_res_file(single_file, store_res)


def analyze_single_res_file(file1, store_res):
    """ this function should create a new data frame for each filename passed as argument and must store those information
     into the store res instance"""

    # return the file name from the path object
    filename = file1.as_posix()
    res_data_frame = pd.read_csv(filename, sep='\t')


def begin_analysis(args_data):
    """ this is the entry point of the analysis """

    # instantiate the root directory and the directories that contain the results
    root_dir = args_data.root_dir
    dir_list = args_data.dir

    home = expanduser("~")
    home_dir_path = Path(home)

    stuck_at_dir_path = home_dir_path / root_dir

    # load the golden prediction file
    gold_prediction = LoadGoldenPrediction("golden_prediction.csv", stuck_at_dir_path)
    gold_pred_df = gold_prediction.get_gpred_dataframe()

    # create a new store results object that should contains the information about the data frame received
    # store_results = StoreResults(gold_pred_df)

    # check if the result directories exists
    if stuck_at_dir_path.exists() and stuck_at_dir_path.is_dir():

        for single_path in dir_list:
            # generate a new path
            new_path = stuck_at_dir_path / single_path / "sim_results"

            # get the file contained into the directory
            dir_reader = MainDirectoryReader(new_path)
            file_list = dir_reader.get_file_list()

    else:
        print("the path specified is not valid")
        return


def arguments_information(args_data):
    # parse the command line arguments
    args_data = arg_parser.parse_args()
    dir_list = args_data.dir
    root_dir = args_data.root_dir

    print("the root dir passed as argument is ", root_dir)

    if dir_list is not None:

        if len(dir_list) != 0:
            for d in dir_list:
                print("dir: ", d)
        else:
            print("the list of dir is empty")

    else:
        print("the dir list has not been defined")


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("root_dir", help="<root-dir> set the root directory taken as starting point for all the "
                                             "evaluation")
    arg_parser.add_argument("--dir", nargs="+", help="<--dir> set the list of directory", required=True)

    # define the arguments
    args = arg_parser.parse_args()
    arguments_information(args)

    # begin_analysis(args)
