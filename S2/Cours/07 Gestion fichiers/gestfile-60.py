from pathlib import Path

data_file = Path(r'.\Travail\tempo\map05.py')

try:
    data_file.unlink()
except IsADirectoryError as e:
    print(f'Error: {data_file} : {e.strerror}')
except FileNotFoundError as e:
    print(f'Error: {data_file} : {e.strerror}')