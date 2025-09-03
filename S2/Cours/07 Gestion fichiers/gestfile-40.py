import os
import fnmatch

for file_name in os.listdir('./Travail/some_directory/'):
    if fnmatch.fnmatch(file_name, '*.txt'):
        print(file_name)
