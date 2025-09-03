def remove_all_before(items, border):
    try:
        return items[items.index(border):]
    except ValueError:
        return items
    
#**********

remove_all_before=lambda i,b:b in i and i[i.index(b):] or i

remove_all_before = lambda i, b: i[i.index(b):] if b in i else i

#**********

from typing import Iterable

def remove_all_before(items: list, border: int) -> Iterable:
    return items[items.index(border):] if border in items else items