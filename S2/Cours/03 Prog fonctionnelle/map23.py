def to_float(number):
    try:
        return float(number.replace(",", "."))
    except ValueError:
        return float("nan")

print(list(map(to_float, ["12.3", "3,3", "-15.2", "One"])))