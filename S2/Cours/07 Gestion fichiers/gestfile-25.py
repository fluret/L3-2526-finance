from pathlib import Path
current_dir = Path('./travail/my_directory')
for path in current_dir.iterdir():
    info = path.stat()
    print(info.st_mtime)