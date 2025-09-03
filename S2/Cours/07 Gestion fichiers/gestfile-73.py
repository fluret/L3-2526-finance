import zipfile

with zipfile.ZipFile(r'.\Travail\data.zip', 'r') as zipobj:
    print(zipobj.namelist())
