import glob
for name in glob.glob('./Travail/some_directory/*[0-9]*.txt'):
    print(name)
