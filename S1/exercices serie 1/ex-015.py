# Créer un tuple d'exemple
exemple_tuple = (1, 2, 3, 4, 5)
print(exemple_tuple)
# Cas où le second indice est plus petit que le premier
slice_inverse = exemple_tuple[3:1]
print(f"Slice avec second indice plus petit que le premier (3:1) : {slice_inverse}")

# Cas où le second indice est plus grand que la taille du tuple
slice_out_of_bounds = exemple_tuple[2:10]
print(f"Slice avec second indice plus grand que la taille du tuple (2:10) : {slice_out_of_bounds}")