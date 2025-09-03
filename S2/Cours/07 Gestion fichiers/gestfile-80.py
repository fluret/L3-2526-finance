import zipfile

file_list = ['./Travail/my_directory/file1.py', './Travail/my_directory/sub_dir/bar.py']
with zipfile.ZipFile(r'.\Travail\new.zip', 'w') as new_zip:
    for name in file_list:
        new_zip.write(name)
