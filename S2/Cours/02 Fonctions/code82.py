def concat(prefix, *args):
    print(f'{prefix}{".".join(args)}')


concat('//', 'a', 'b', 'c')
concat('... ', 'foo', 'bar', 'baz', 'qux')