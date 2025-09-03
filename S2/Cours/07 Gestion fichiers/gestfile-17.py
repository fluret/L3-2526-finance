from pathlib import Path

# List all files in directory using pathlib
basepath = Path('./travail/my_directory/')
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files_in_basepath:
    print(item.name)
