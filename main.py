import argparse

from pathlib import Path
from os.path import expanduser
from loadGoldenPrediction import LoadGoldenPrediction
from loadResultFile import LoadResultFile


'''def create_new_plot():
        plt.plot([1, 2, 3], [9, 89, 10])
        plt.ylabel('y-axis')
        plt.xlabel('x-axis')
        plt.show() 
'''


def analyze_single_res_dir(dir_path, file_list):
    """ pass as argument to this function the list of the file contained into a single directory """

    for single_file in file_list:
        analyze_single_res_file(single_file, dir_path)


def analyze_single_res_file(file1, path):
    """ this function should create a new data frame for each filename passed as argument and must store those information
     into the store res instance """

    # load the file
    res_file = LoadResultFile(file1, path)
    df = res_file.res_data_frame


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
    gold_pred_df = gold_prediction.get_gold_pred_data_frame()

    analyzer = AnalyzeResults(stuck_at_dir_path, dir_list, gold_pred_df)

    '''# check if the result directories exists
    if stuck_at_dir_path.exists() and stuck_at_dir_path.is_dir():

        for single_path in dir_list:
            # generate a new path for every entry into the dir_list
            new_path = stuck_at_dir_path / single_path / "sim_results"

            # get the file contained into the directory
            dir_reader = MainDirectoryReader(new_path)
            file_list = dir_reader.get_file_list()

            # pass the file list contained into the directory
            analyze_single_res_dir(file_list, store_results)

    else:
        print("the path specified is not valid")
        return
        
    '''


def arguments_information(args_data):
    # parse the command line arguments
    args_data = arg_parser.parse_args()
    dir_list = args_data.dir
    output_folder = args_data.output
    fault_model = args_data.fault_model

    # print the information about the output folder and the fault model to be used
    print("the output folder specified is ", output_folder)
    print("the fault model specified is ", fault_model)

    if dir_list is not None or len(dir_list) == 0:

        if len(dir_list) != 0:
            for d in dir_list:
                print("dir: ", d)
        else:
            print("the list of dir is empty")

    else:
        print("the dir list has not been defined")


if __name__ == "__main__":

    # decode the argument passed to the script
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("fault_model", help="specify the fault model")
    arg_parser.add_argument("--dir", nargs="+", help=" set the list of directory", required=True)
    arg_parser.add_argument("--out", help="specify the output folder for the analysis results", required=True)

    # define the arguments
    args = arg_parser.parse_args()
    arguments_information(args)

    if args.fault_model == "stuck-at":
        pass
    else:
        print("the fault model specified is", args.fault_model)
        print("other fault model analysis are not yet implemented")

    # begin_analysis(args)
