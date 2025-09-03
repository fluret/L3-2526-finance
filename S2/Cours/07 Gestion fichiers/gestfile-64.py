import shutil

trash_dir = r'.\Travail\tempo\essai3'

try:
    shutil.rmtree(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')