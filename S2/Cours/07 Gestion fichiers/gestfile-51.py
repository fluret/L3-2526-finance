import os
for dirpath, dirnames, files in os.walk('./Travail/directory_walk/', topdown=False):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)
