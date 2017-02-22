import os
import shutil
import re
import argparse
'''
Moves every file with .mkv extension from subfolders to
main folder defined in root variable.
'''
root = "" # e.g. 'G:\Filmy\Narcos S02'
file_extensions = [] #e.g. ['.mkv','.avi']


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("path",help="Full path to root directory")
    parser.add_argument("-ext",nargs="+", help="Searched extension")
    args = parser.parse_args()
    return args

def move_files_to_main_folder_from_subfolders(extension,main_folder_path):
    for path, subdirs, files in os.walk(main_folder_path):
        for name in files:
            if ((re.search(extension,name) != None) and (len(path) > len(main_folder_path))):
                full_file_path =  os.path.join(path, name)
                print full_file_path
                shutil.move(full_file_path,main_folder_path)

def main():
    opts = parse_args()
    root = opts.path
    file_extensions.extend(opts.ext)
    print(file_extensions)
    print(root)
    print("Files with given extension are extracted from: %s" %root)
    os.chdir(root)
    for file_extension in file_extensions:
        move_files_to_main_folder_from_subfolders(file_extension,root)


if __name__ == '__main__':   
    main()