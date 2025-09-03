import zipfile

with zipfile.ZipFile(r'.\Travail\data.zip', 'r') as zipobj:
    bar_info = zipobj.getinfo('zip_directory/sub_dir/bar.py')
    print(bar_info.file_size)
