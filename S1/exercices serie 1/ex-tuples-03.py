
def trouve(tup, element):
    for index, value in enumerate(tup):
        if value == element:
            return index
    return -1

exemple_tuple = (1, 2, 3, 4, 5)

ELEMENT_A_TROUVER = 3
poisition = trouve(exemple_tuple, ELEMENT_A_TROUVER)

print(f"L'élément {ELEMENT_A_TROUVER} se trouve à la position {poisition} dans le tuple {exemple_tuple}")

ELEMENT_A_TROUVER = 6

poisition = trouve(exemple_tuple, ELEMENT_A_TROUVER)    

print(f"L'élément {ELEMENT_A_TROUVER} se trouve à la position {poisition} dans le tuple {exemple_tuple}")


