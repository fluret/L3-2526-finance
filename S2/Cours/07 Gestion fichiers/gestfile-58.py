import os

data_file = r'.\Travail\tempo\map03.py'

if os.path.isfile(data_file):
    os.remove(data_file)
else:
    print(f'Error: {data_file} not a valid filename')