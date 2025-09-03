def checkio(number):
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res

#**********

checkio = lambda n: eval("*".join(i for i in str(n) if i != '0'))

#**********

def checkio(number):
    total = 1
    for i in str(number).replace("0",""):
        total *= int(i)
    return total

