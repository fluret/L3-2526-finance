import zipfile
import os

data_zip = zipfile.ZipFile(r'.\Travail\data.zip', 'r')
data_zip.extract(r'zip_directory\file1.py', r'.\Travail\extract_dir1')
data_zip.extractall(path=r'.\Travail\extract_dir2', )
data_zip.close()