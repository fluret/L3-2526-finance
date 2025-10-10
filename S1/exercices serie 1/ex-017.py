def trouve_min_max(tup):
    """Renvoie un tuple contenant le plus petit et le plus grand entier du tuple."""
    if not tup:  # Vérifier si le tuple est vide
        return None, None
    min_val = min(tup)
    max_val = max(tup)
    return min_val, max_val


# Exemple d'utilisation
exemple_tuple = (1, 2, 3, 4, 5)
min_max = trouve_min_max(exemple_tuple)
print(f"Le plus petit et le plus grand entier du tuple sont : {min_max}")

exemple_tuple_vide = ()
min_max_vide = trouve_min_max(exemple_tuple_vide)
print(f"Le plus petit et le plus grand entier du tuple vide sont : {min_max_vide}")