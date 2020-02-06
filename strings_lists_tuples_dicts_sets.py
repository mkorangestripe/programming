# Strings

import string
print string.ascii_lowercase #  abcdefghijklmnopqrstuvwxyz
print string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ

text1 = '123\nABC'
text1.split('\n') # ['123', 'ABC']
'\n'.join(['123', 'ABC']) # '123\nABC'

# String formatting
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print '{0:10} ==> {1:10d}'.format(name, phone)
# Dcab       ==>       7678
# Jack       ==>       4098
# Sjoerd     ==>       4127

# Parses string, keeping together items in quotes
import shlex
body = '''This string has embedded "double quotes" and 'single quotes' in it, and even "a 'nested example'".'''
print('ORIGINAL:', repr(body))
# ('ORIGINAL:', '\'This string has embedded "double quotes" and \\\'single quotes\\\' in it, and even "a \\\'nested example\\\'".\'')
lexer = shlex.shlex(body)
for token in lexer:
   print repr(token)
# 'This'
# 'string'
# 'has'
# 'embedded'
# '"double quotes"'
# 'and'
# "'single quotes'"
# 'in'
# 'it'
# ','
# 'and'
# 'even'
# '"a \'nested example\'"'
# '.'



# Lists

# Print index and values of list
cassandra_endpoints=['10.141.18.229', '10.141.18.214', '10.141.18.219']

# enumerate
for i, v in enumerate(cassandra_endpoints):
    print i, v
# 0 10.141.18.229
# 1 10.141.18.214
# 2 10.141.18.219

# list.index method
for endpoint in cassandra_endpoints:
    print cassandra_endpoints.index(endpoint), endpoint
# 0 10.141.18.229
# 1 10.141.18.214
# 2 10.141.18.219

# Sorted
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
sorted(basket)
# ['apple', 'apple', 'banana', 'orange', 'orange', 'pear']

# Self referencing list
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
print selfref_list
# [1, 2, 3, [...]]
print selfref_list[3][1]
# 2

# Creates a list of tuples with corresponding pairs
letters = ['a', 'b', 'c']
numbers = ['1', '2', '3']
zip(letters, numbers)
# [('a', '1'), ('b', '2'), ('c', '3')]

# List Comprehension

# Create a list of squares:
print [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Combines the elements of two lists if they are not equal.
print [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# The above as a for-loop:
list1 = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            list1.append((x,y))
print(list1)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# List comprehensions can contain complex expressions and nested functions.
from math import pi
[str(round(pi, i)) for i in range(1, 6)]
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']



# Named tuples
from collections import namedtuple
Point = namedtuple('Redpoint', 'x y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)
print pt1
# Redpoint(x=1.0, y=5.0)
print pt2
# Redpoint(x=2.5, y=1.5)



# Dictionaries

# Either of these creates a dictionary.
d1 = dict(one=1, two=2, three=3, four=None)
d1 = {'one': 1, 'two': 2, 'three': 3, 'four': None}

# List keys:
d1.keys()
# ['four', 'three', 'two', 'one']

# List values:
d1.values()
# [None, 3, 2, 1]

# Test whether an element exists.
print 'five' in d1
# False
d1.has_key('five')
# False

# Get a value and avoid a KeyError if an element doesn't exist.
d1.get('three')
# 3
d1.get('five', 0)
# 0
print d1.get('five')
# None

# Prints keys and corresponding values of a dictionary
dict1 = {'a':'d', 'b':'e'}
for k, v in dict1.iteritems():
    print k, v
# a d
# b e

# Reverse dictionary keys and values using zip
dict1 = {'a':'d', 'b':'e'}
dict(zip(dict1.values(),dict1.keys()))
# {'d': 'a', 'e': 'b'}

# OrderedDict
from collections import OrderedDict
d1 = OrderedDict()
d1['foo'] = 1
d1['bar'] = 2
d1['spam'] = 3
d1['grok'] = 4
print d1
# OrderedDict([('foo', 1), ('bar', 2), ('spam', 3), ('grok', 4)])



# Sets, Frozensets

# http://docs.python.org/2/library/sets.html
engineers = set(['John', 'Jane', 'Jack', 'Janice'])
programmers = set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = set(['Jane', 'Jack', 'Susan', 'Zack'])

# union
print engineers | programmers | managers
# set(['Jack', 'Sam', 'Susan', 'Jane', 'Janice', 'John', 'Zack'])

# intersection
print engineers & managers
# set(['Jane', 'Jack'])

# difference
print managers - engineers - programmers
# set(['Zack'])

# Add item
engineers.add('Marvin')
print engineers
# set(['Jane', 'Marvin', 'Janice', 'John', 'Jack'])

# Superset
employees = engineers | programmers | managers
print employees.issuperset(engineers)
# False

# Update from another set and retest:
employees.update(engineers)
print employees.issuperset(engineers)
# True

# Unconditionally remove an element:
for group in [engineers, programmers, managers, employees]:
    group.discard('Susan')

# Create an immutable set:
engineers = frozenset(engineers)

# Sort alphabetically and uniquely, similar to 'sort -u'
sorted(set(basket))
