import fnmatch
import os
import sys

from progressbar import ProgressBar

pbar = ProgressBar()  # just a progressbar --> not essential for the solution


def find_files(start_dir: str, filename: str) -> list:
    file_list = list()
    # for path, dirs, files in os.walk(start_dir):       # without progressbar
    for path, dirs, files in pbar(os.walk(start_dir)):
        if filename in files:
            full_path_name = os.path.join(path, filename)
            file_list.append(full_path_name)

    return file_list or None


def find_witht_wildcards(start_dir: str, filename: str) -> list:
    file_list = list()
    # for path, dirs, files in os.walk(start_dir):       # without progressbar
    for path, dirs, files in pbar(os.walk(start_dir)):
        for file in files:
            if fnmatch.fnmatch(file, filename):  # fnmatch(name , patern)
                full_path_name = os.path.join(start_dir, file)
                file_list.append(full_path_name)

    return file_list or None


# Main section -----------------------
if len(sys.argv) == 3:
    root_dir = sys.argv[1]
    file_to_search = sys.argv[2]
    print("\n ARGs = ", *sys.argv)
    print('\n')

    if '*' in file_to_search:
        find_results = find_witht_wildcards(root_dir, file_to_search)
    else:
        find_results = find_files(root_dir, file_to_search)

    # for entry in find_results:
    #     print(entry)
    print(*find_results, sep='\n')
    print("\n {} matches found! \n".format(len(find_results)))
else:
    print("Please provide a dir as a first parameter and filename as a second ")
