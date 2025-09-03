import glob
for file in glob.iglob('./Travail/some_directory/**/*.py', recursive=True):
    print(file)
