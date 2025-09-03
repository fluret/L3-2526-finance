from datetime import datetime, timezone
from os import scandir

def convert_date(timestamp):
    d = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    formated_date = d.strftime('%d %b %Y %H:%M:%S %Z')
    return formated_date

def get_files():
    with scandir('./travail/my_directory/') as dir_entries:
        for entry in dir_entries:
            if entry.is_file():
                info = entry.stat()
                print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')

get_files()