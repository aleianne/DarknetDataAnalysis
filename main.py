import numpy as np 
import matplotlib.pyplot as plt
from os.path import expanduser

from mainDirReader import MainDirReader

def main_script():
    print("ciao")


def create_new_plot():
    plt.plot([1, 2, 3], [9, 89, 10])
    plt.ylabel('y-axis')
    plt.xlabel('x-axis')
    plt.show()


def begin_analysis():
    ''' this is the entry point of the analysis '''

    # define configuration data about the result directory
    home = expanduser("~")
    homeDirPath = Path(home)

    documentsDirPath = homeDirPath / "documents"
    stuck-atDirPath = documentsDirpath / "s-a-sim"

    # define a new list that contains the sim result list
    dir_list = []
    for i in range(1, 8):
        dir_name = "dir_" + str(i)
        dir_list.append(dir_name)

    # load the golden prediction file
    gold_prediction = LoadGoldenPrediction("golden_prediction.csv", stuck-atDirPath)
    goldPredDF gold_prediction.get_gpred_dataframe()

    # check if the result directories exists
    if (stuck-atDirPath.exists() and stuck-atDirPath.is_dir()):

        for single_path in dir_path:
            # generate a new path
            new_path = stuck-atDirPath / single_path / "sim_results"

            # get the file contained into the directory
            dirReader = MainDirectoryReader(new_path)

            file_list = dirReader.get_file_list()
            

    else:
        print("the path specified is not valid")
        return
    

if __name__ == "__main__":
    main_script()