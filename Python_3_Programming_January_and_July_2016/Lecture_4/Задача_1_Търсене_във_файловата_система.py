"""
Напишете програма, която търси за файлове във Вашата файлова система. Програмата трябва да получава два параметъра
при извикването - къде да търси, и какво да търси.
Примерно извикване на програмата:
                                    python3  find.py  /home/user/Downloads  me.jpg

В този случай find.py е името на скрипта, /home/user/Downloads в коя папка да се търси, и me.jpg е името на търсения файл.
Търсенето трябва да да включва всички поддиректории, които се намират в началната директория за търсене.
Ако файлът не е намерен, трябва да се показва съобщение, че файлът не е намерен. В противен случай трябва да се отпечата пълния път до файла.
Ако има повече от един файл със същото име в различни директории трябва да се покаже списък с всички намерени файлове.

Ако сте готови с решението на задачата, можете да направите програмата малко по-полезна,
като реализирате възможност да търсите с прост wild card * - в началото или в края на името.
Пример:
        python3   find.py   /home/Downloads   me*
В примера по-горе кодът ще трябва да намери всички файлове, чието име започва с me, без значение какви символи следват след това.
"""

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
# if len(sys.argv) == 3:
if sys.argv[2] and os.path.isdir(sys.argv[1]):
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
