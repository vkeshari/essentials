import sys
sys.exit("Reference material. Do not execute.")


### builtin fns ###

max([1, 2, 3])
min([1, 2, 3])
round(1.2)


### str ###

s = 'Hello'
s.find('l') # --> 2

# String formatting
'My name: %s, my age: %3d, my favorite number: %5.2f' \
        % ('Virat', 35, 5.555)

'My name: {name}, my age: {age:3d}, my favorite number: {num:5.2f}. I am {name}.' \
        .format(name = 'Virat', age = 35, num = 5.555)


### list ###

l = [1, 2, 3]
l.append(4)
l.pop() # --> 4
del l[0]

m = [1, 3, 2]
sorted(m, reverse = True) # --> [3, 2, 1]
reversed(m) # --> [2, 3, 1]

# Iterating
for i, v in enumerate(l):
  pass

# Create list from generators
list(range(0, 10, 2))


### tuple ###

t = 1, 2, 3
t = tuple([1, 2, 3])


### set ###

s = set()
s = set([1, 2, 3])
t = {2, 3, 4}

# Set operations
s - t
s & t # boolean operators & | and ^


### dict ###

d = {1 : 'a', 2: 'b'}
d.keys() # Returns a set
d.values()
d.items() # tuple

del d[2]

sorted(d) # sorted keys
dict(sorted(d.items())) # sorts by key

# Sort by a value or sub-value in dict
dict(sorted(d.items() , key = lambda i: i[1], reverse = True))

# Sort by multiple keys
dict(sorted(d.items() , key = lambda i: (i[1]['rank'], -i[1]['score']))) # Use -neg for reverse

# Create a custom sort key on nested items of arbitrary length
def get_sort_key(keys):
  sort_key = '('
  for k in keys:
    sort_key += "i[1][" + repr(k) + "],"
  sort_key += ')'
  return sort_key

ranges = {'range1': (1, 5), 'range2': (2, 4), 'range3': (2, 3)}
ranges_val_keys = [1, 0] # indices of nested tuples
sort_key = get_sort_key(ranges_val_keys) # --> """(i[1][1], i[1][0],)"""

sorted_ranges = sorted(ranges, key = lambda i: eval(sort_key), reverse = True)


### zip ###

l = [(1, 2), (3, 4)]
list( zip(*l) ) # --> [(1, 3), (2, 4)]


### lambda ###

f = lambda i : i + 1 # only one expression allowed
h = f(i = 5) # --> 6

g = lambda i, j = 1 : i + j # multiple variables with defaults allowed
h = g(2, 3) # --> 5
h = g(2)    # --> 3

# Create custom lambda from function
def make_mul(n):
  return lambda i: i * n
mul_2 = make_mul(2)
mul_2(4) # --> 8


### transform ###

# filter
f = list( filter(lambda i : i > 0, [-1, 0, 1]) ) # --> [1]

# map
m = list( map(lambda i: i + 1, [-1, 0, 1]) ) # --> [0, 1, 2]

# reduce
from functools import reduce
r = reduce (lambda i, j: i + j, [1, 2, 3])    # --> 6
r = reduce (lambda i, j: i + j, [1, 2, 3], 4) # --> 10


### file ###

with open(read_filename) as f:
  lines = f.readlines()

with open('workfile', 'w', encoding = 'utf-8') as f:
  f.write('abc\n')


### yield ###

# Lazily process a long CSV file
def yields_lines(filename):
  with open(filename, 'r') as f:
    l = f.readline()
    while l:
      yield l.strip().split(',')
      l = f.readline()

for l in yield_lines('my_data.csv'):
  pass


### math ###
import math

math.inf
math.nan
math.e
math.pi

math.sqrt(100) --> 10
math.log(100, 10) --> 2
math.pow(3, 2) --> 9
math.exp(2) --> math.e ^ 2
