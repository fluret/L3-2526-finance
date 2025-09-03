import zipfile

with zipfile.ZipFile('secret.zip', 'r') as pwd_zip:
    pwd_zip.extractall(path='extract_dir', pwd='Quish3@o')