import functools
import operator
import os

directory = "c:\\tempo\\"
files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

print(functools.reduce(operator.add, map(os.path.getsize, files)))