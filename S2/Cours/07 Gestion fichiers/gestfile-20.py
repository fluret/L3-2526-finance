import os

# List all subdirectories using scandir()
basepath = './travail/my_directory/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)