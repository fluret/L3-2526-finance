import os

data_file = r'.\Travail\tempo\map04.py'

# Use exception handling
try:
    os.remove(data_file)
except OSError as e:
    print(f'Error: {data_file} : {e.strerror}')