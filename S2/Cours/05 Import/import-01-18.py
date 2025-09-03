s = 'foo'
a = ['foo', 'bar', 'baz']

from mod import s as string, a as alist
print(s)
print('foo')
print(string)
print(a)
print(alist)