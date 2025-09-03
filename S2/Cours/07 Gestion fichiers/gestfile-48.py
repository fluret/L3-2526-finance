from pathlib import Path
p = Path('./Travail/some_directory/')
for name in p.glob('*.p*'):
    print(name)