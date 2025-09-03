import os

for dirpath, dirnames, files in os.walk(r'.\Travail\tempo\essai', topdown=False):
    try:
        os.rmdir(dirpath)
    except OSError:
        pass