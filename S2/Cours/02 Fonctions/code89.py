def concat(*args, prefix='-> ', sep='.'):
    print(f'{prefix}{sep.join(args)}')


concat('a', 'b', 'c')
concat('a', 'b', 'c', prefix='//')
concat('a', 'b', 'c', prefix='//', sep='-')