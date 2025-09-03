from pathlib import Path

trash_dir = Path(r'.\Travail\tempo\essai2')

try:
    trash_dir.rmdir()
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')