x = 20
def f():
    global x
    x = 40
    print(x)

f()
print(x)