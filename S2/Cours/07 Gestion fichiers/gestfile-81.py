import zipfile

with zipfile.ZipFile(r'.\Travail\new.zip', 'a') as new_zip:
    new_zip.write('./Travail/my_directory/file2.csv')
    new_zip.write('./Travail/my_directory/file3.txt')
