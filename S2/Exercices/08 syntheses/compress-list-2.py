from itertools import groupby

def compress(items):
    for key, _ in groupby(items): yield key
    
#**********

import itertools
compress = lambda l: (i for i, _ in itertools.groupby(l))

#**********

compress= lambda x: [x[i] for i in range(len(x)) if i==0 or x[i]!=x[i-1]]

