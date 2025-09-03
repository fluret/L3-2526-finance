import zipfile

with zipfile.ZipFile(r'.\Travail\data.zip', 'r') as zipobj:
    bar_info = zipobj.getinfo('zip_directory/sub_dir/bar.py')
    print(bar_info.file_size)
    print(bar_info.date_time)
    print(bar_info.compress_size)
    print(bar_info.filename)
