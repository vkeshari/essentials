import sys
sys.exit("Reference material. Do not execute.")

### tuple ###

t = tuple([1, 2, 3])


### dict ###

d = {1 : 'a', 2: 'b'}
d.keys()
d.values()
d.items() # tuple

sorted(d) # sorted keys
dict(sorted(d.items())) # sorts by key

# Sort by a value or sub-value in dict
dict(sorted(i for i in d.items() , key = i[1], reverse = True))


### zip ###

l = [(1, 2), (3, 4)]
list( zip(*l) ) # --> [(1, 3), (2, 4)]


### lambda ###

f = lambda i : i + 1 # only one expression allowed
h = f(i = 5) # --> 6

g = lambda i, j = 1 : i + j # multiple variables with defaults allowed
h = g(2, 3) # --> 5
h = g(2)    # --> 3


### transform ###

# filter
f = list( filter(lambda i : i > 0, [-1, 0, 1]) ) # --> [1]

# map
m = list( map(lambda i: i + 1, [-1, 0, 1]) ) # --> [0, 1, 2]

# reduce
from functools import reduce
r = reduce (lambda i, j: i + j, [1, 2, 3])    # --> 6
r = reduce (lambda i, j: i + j, [1, 2, 3], 4) # --> 10
