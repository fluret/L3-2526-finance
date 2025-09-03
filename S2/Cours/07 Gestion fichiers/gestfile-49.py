import os

# Walking a directory tree and printing the names of the directories and files
for dirpath, dirnames, files in os.walk('./Travail/directory_walk/'):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)
