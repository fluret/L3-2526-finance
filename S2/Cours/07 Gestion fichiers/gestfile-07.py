import os

with os.scandir('./travail/my_directory/') as entries:
    for entry in entries:
        print(entry.name)
