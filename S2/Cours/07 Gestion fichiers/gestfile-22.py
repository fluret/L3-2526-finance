from pathlib import Path

# List all subdirectory using pathlib
basepath = Path('./travail/my_directory/')
for entry in basepath.iterdir():
    if entry.is_dir():
        print(entry.name)
