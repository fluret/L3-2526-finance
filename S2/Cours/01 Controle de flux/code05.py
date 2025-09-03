a = ['foo', 'bar', 'baz', 'qux']
s = 'corge'

i = 0
while i < len(a):
    if a[i] == s:
    # Processing for item found
        break
    i += 1
else:
    # Processing for item not found
    print(s, 'not found in list.')