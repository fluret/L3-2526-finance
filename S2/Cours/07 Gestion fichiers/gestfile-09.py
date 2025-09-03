from pathlib import Path

entries = Path('./travail/my_directory/')
for entry in entries.iterdir():
    print(entry.name)
