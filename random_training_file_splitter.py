import random
import os
import glob
import argparse


# Find all files in dir with extension (to exclude other files)
def find_files_in(path, with_extension = ""):
    pattern = path + "/*." + with_extension
    return glob.glob(pattern)


# Makes directories
def make_dirs(path, train_dir_name = 'train', test_dir_name = 'test'):
    for dir_name in [train_dir_name, test_dir_name]:
        try:
            os.mkdir(path + "/" + dir_name)
        except OSError:
            print ("Creation of the directory %s failed" % path + "/" + dir_name)
        else:
            print ("Successfully created the directory %s " % path + "/" + dir_name)


# Selects randomly the files according to a preset policy
# Moves the files
def random_select(list_of_files, percentage_split, train_dir_path, test_dir_path):
    for file in list_of_files:
        path, filename = os.path.split(file)

        choices = ['test'] * int((percentage_split * 100)) + ['train'] * int(((1 - percentage_split) * 100))

        choice = random.choice(choices)

        is_training = choice == 'train'

        # Search for similar files to move them as well
        pattern = path + "/" + os.path.splitext(filename)[0] +".*"
        files = glob.glob(pattern)
        for file_i in files:
            _ , filename_i = os.path.split(file_i)
            if is_training:
                os.rename(file_i, train_dir_path + "/" + filename_i)
            else:
                os.rename(file_i, test_dir_path + "/" + filename_i)


def main(path, train_dir_name = "train", test_dir_name = "test", file_extension = "jpg", split_strategy = 0.5):
    file_paths = find_files_in(path, file_extension)
    make_dirs(path,train_dir_name, test_dir_name)
    random_select(file_paths, split_strategy, path + "/" + test_dir_name, path + "/" + train_dir_name)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--path', type=str,
        help='path to images ',
        default=os.getcwd()
    )

    parser.add_argument(
        '--train_dir_name', type=str,
        help='Name of train data directory name ',
        default='train'
    )

    parser.add_argument(
        '--test_dir_name', type=str,
        help='Name of test data directory name ',
        default='test'
    )

    parser.add_argument(
        '--file_extension', type=str,
        help='The extension of the file you want to get handled ',
        default='jpg'
    )

    parser.add_argument(
        '--split_strategy', type=float,
        help='Percentage of split strategy to split training and test data ',
        default=0.5
    )

    args = vars(parser.parse_args())

    main(args["path"],args["train_dir_name"], args["test_dir_name"], args["file_extension"],
         args["split_strategy"])
