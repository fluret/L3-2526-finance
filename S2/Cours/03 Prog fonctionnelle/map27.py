import os
directory = "c:\\tempo\\"
files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

print(sum(map(os.path.getsize, files)))