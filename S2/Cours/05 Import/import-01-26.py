print(dir())

import mod
print(dir())

print(mod.s)

mod.foo([1, 2, 3])

from mod import a, Foo
print(dir())

print(a)

x = Foo()
print(x)

from mod import s as string
print(dir())

print(string)