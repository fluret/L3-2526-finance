import os

# Get .txt files
for f_name in os.listdir('./Travail/some_directory'):
    if f_name.endswith('.txt'):
        print(f_name)