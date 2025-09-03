from pathlib import Path

p = Path('./travail/example_directory')
try:
    p.mkdir()
except FileExistsError as exc:
    print(exc)
