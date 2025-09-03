def concat(*args, prefix):
  print(f'{prefix}{".".join(args)}')

concat('a', 'b', 'c', prefix='... ')

concat('a', 'b', 'c')