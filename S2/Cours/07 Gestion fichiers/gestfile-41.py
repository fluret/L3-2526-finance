import os
import fnmatch

for filename in os.listdir('./Travail/some_directory/'):
    if fnmatch.fnmatch(filename, 'data_*_backup.txt'):
        print(filename)
