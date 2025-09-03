import os

trash_dir = r'.\Travail\tempo\essai1'

try:
    os.rmdir(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')