import argparse

from loadGoldenPrediction import LoadGoldenPrediction
from loadDataFrame import LoadDataFrame
from stuckAtResultAnalysis import StuckAtResultAnalysis
from utils.constant import CLASSIFICATION_FILENAME, WRONG_LABELS_FILENAME


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
    res_file = LoadDataFrame(file1)
    # df = res_file.res_data_frame


def begin_analysis(args_data):
    """ this is the entry point of the analysis """

    # instantiate the root directory and the directories that contain the results
    # root_dir = args_data.root_dir
    # dir_list = args_data.dir
    #
    # home = expanduser("~")
    # home_dir_path = Path(home)
    #
    # stuck_at_dir_path = home_dir_path / root_dir
    #
    # # load the golden prediction file
    # gold_prediction = LoadGoldenPrediction("golden_prediction.csv", stuck_at_dir_path)
    # gold_pred_df = gold_prediction.get_gold_pred_data_frame()
    #
    # analyzer = AnalyzeResults(stuck_at_dir_path, dir_list, gold_pred_df)

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
    output_folder = args_data.out
    operation = args_data.operation
    golden_prediction = args_data.gold

    # print the information about the output folder and the fault model to be used
    print("the golden prediction file is", golden_prediction)
    print("the output folder specified is ", output_folder)
    print("the operation specified is ", operation)

    if dir_list is not None or len(dir_list) == 0:

        if len(dir_list) != 0:
            for d in dir_list:
                print("dir: ", d)
        else:
            print("the list of dir is empty")

    else:
        print("the dir list has not been defined")


def print_graphics(args_data):
    dir_list = args_data.dir
    output_dir = args_data.out
    file_dir = None

    if isinstance(dir_list, list) and len(dir_list) == 1:
        file_dir = dir_list.pop()
    else:
        print("impossible to decode the dir option")
        return

    # create a new LoadGraphicsDataFrame
    # graphics_plotter = GraphWriter()
    # graphics_plotter.load_new_data_frame_2(CLASSIFICATION_FILENAME, WRONG_LABELS_FILENAME)
    # graphics_plotter.create_new_graphics()
    # graphics_plotter.show_figures()


def begin_stuck_at_fault_analysis(args_data):

    dir_list = args_data.dir
    output_dir = args_data.out
    gold_file = args_data.gold

    gold_prediction_loader = LoadGoldenPrediction(gold_file)
    gold_prediction_loader.load_golden_prediction_df(1)

    # instantiate a new stuck at result analyzer
    fault_analyzer = StuckAtResultAnalysis(dir_list, gold_prediction_loader.get_gold_pred_data_frame())
    # gold_prediction_loader.print_golden_prediction_df()
    # fault_analyzer = StuckAtResultAnalysis(args_data.dir, None)

    # begin to load the files
    fault_analyzer.load_files()
    fault_analyzer.debug()

    # fault_analyzer.print_all_files()
    # fault_analyzer.analyze_stuck_at_faults()
    #
    # # save all the data frames into a file
    # fault_analyzer.save_data_frames_into_csv(output_dir)


if __name__ == "__main__":

    # decode the argument passed to the script
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("operation", help="specify the fault model")
    arg_parser.add_argument("--gold", help="set the path of the golden prediction file")
    arg_parser.add_argument("--dir", nargs="+", help=" set the list of directory")
    arg_parser.add_argument("--out", help="specify the output folder for the analysis results")

    # define the arguments
    args = arg_parser.parse_args()
    # arguments_information(args)

    if args.operation == "stuck-at":

        if args.dir is None or args.out is None or args.gold is None:
            print("stuck at usage: [--dir dir_list], [--gold golden_prediction_file], [--out output dir]")
        else:
            begin_stuck_at_fault_analysis(args)

    elif args.operation == "print_graphics":

        if args.dir is None or args.out is None:
            print("print graphics usage: [--dir dir], [--out output dir]")
        else:
            print_graphics(args)

    else:
        print("the fault model specified is", args.fault_model)
        print("other fault model analysis are not yet implemented")

    # begin_analysis(args)
