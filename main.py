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
    plt.show() '''


def analyze_single_res_dir(file_list, store_res):
    ''' pass as argument to this function the list of the file contained into a single directory '''

    for f in file_list:
        analyze_single_res_file(f, store_res)


def analyze_single_res_file(file1, store_res):
    '''this function should create a new dataframe for the file passed as argument
    also pass as argument the store res object, in order to retrieve the data from the memory '''

    # return the filaname from the path object
    filename = file1.as_posix()
    resDataFrame = pd.read_csv(filename, sep='\t')


def begin_analysis(dir_list, dir_root):
    ''' this is the entry point of the analysis '''

    # define configuration data about the result directory
    home = expanduser("~")
    home_dir_path = Path(home)

    stuck_at_dir_path = home_dir_path / dir_root

    # load the golden prediction file
    gold_prediction = LoadGoldenPrediction("golden_prediction.csv", stuck_at_dir_path)
    goldPredDF = gold_prediction.get_gpred_dataframe()

    # create a new store results object that should contains the informations about the dataframe received
    # store_results = StoreResults(goldPredDF)

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
    

if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("root_dir", help="<root-dir> set the root directory taken as starting point for all the "
                                             "evaluation")
    arg_parser.add_argument("--dir", nargs="+", help="<--dir> set the list of directory", required=True)

    # parse the command line arguments
    arg = arg_parser.parse_args()
    dir_list = arg_parser.dir
    root_dir = arg_parser.root_dir

    begin_analysis()
