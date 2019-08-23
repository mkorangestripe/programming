# Sets the python path before running the shell:
# PYTHONPATH=./src ipython


# Convert between chr and int (integer ordinal):
ord('A') # 65
chr(65) # A
# Convert between hex and int
int(0x41) # 65
hex(65) # 0x41
# Convert between bin and int
int(0b1000001) # 65
bin(65) # 0b1000001
# Convert between oct and int
int(0101) # 65
oct(65) # 0101

# Multiple assignment:
a, b = 9, 2

# Return a list of valid attributes for the object:
dir(list)

# Use a global variable in a function:
global num



# Random

import random

# Random float x, 0.0 <= x < 1.0
random.random() # 0.9077696509551497

# Random float x, 1.0 <= x < 10.0
random.uniform(1, 10) # 6.38304208099131

# Integer from 1 to 10, endpoints included
random.randint(1, 10) # 7

# Integer from 0 to 359
random.randrange(360) # 119

# Even integer from 0 to 100
random.randrange(0, 101, 2) # 70

# Choose a random element
random.choice('abcdefghij') # h

# Choose 3 elements
items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
# [7, 3, 5, 2, 1, 4, 6]
random.sample([1, 2, 3, 4, 5],  3)
# [5, 3, 2]



# A way to send a password with some security using hashing.

# Computer1
import string, random, hashlib
numbers_letters = string.digits + string.ascii_letters
randomString = ''.join(random.sample(numbers_letters,  8))
hash = hashlib.sha1(randomString).hexdigest()
hashpass = hash[-10:-2] # To limit the password to an arbitrary 8 characters.
# Set the user's password to hashpass.
# Send the random string to Computer 2.

# Computer2
import hashlib
randomString = "The random string from Computer1"
hash = hashlib.sha1(randomString).hexdigest()
hashpass = hash[-10:-2]
# Login to Computer1 using hashpass as the password.



# time, date

# Time in seconds since the epoch
import time
time.time() # 1554133995.335201

# Date in YYYYMMDD format
import time
date = time.strftime('%Y%m%d')
print date
# similar to 20190516

import datetime
now = datetime.datetime.now()
now_plus_one_day = now + datetime.timedelta(days = 1)
date_plus_one_day = now_plus_one_day.strftime('%Y%m%d%H%M')
print date_plus_one_day
# similar to 201905171155



# Regex

# r is for 'raw string', \w is for 'word character'
import re
string1 = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', string1)
print match.group()
# word:cat

import re
string2 = 'apple\\orange'
match = re.search(r'\\', string2)
print match.group()
# \



# Reversed
for i in reversed(xrange(1,11)):
    print i,
# 10 9 8 7 6 5 4 3 2 1



# Generators, Yield:

# Generators are iterators, but can only be iterated over once.
generator1 = (x**2 for x in range(10))
for i in generator1: print i,
# 0 1 4 9 16 25 36 49 64 81
for i in generator1: print i,
# Nothing is printed

# Yield:
# Yield returns a generator.
# Unlike a list, the cubes generator doesn't store any of these items in memory,
# rather the cubed values are computed at runtime, returned, and forgotten.
def cube_numbers(nums):
    for i in nums:
        yield(i**3)

cubes = cube_numbers([1, 2, 3, 4, 5])
next(cubes) # 1
next(cubes) # 8
next(cubes) # 27



## Hashing
## http://en.wikipedia.org/wiki/Hash_function
## A hash function is any algorithm that maps data of variable length to data of a fixed length.
## The values returned by a hash function are called hash values, hash codes, hash sums, checksums or simply hashes.
## Hash functions are primarily used in hash tables, to quickly locate a data record.
## http://en.wikipedia.org/wiki/Hash_table
## In a well-dimensioned hash table, the average cost (number of instructions) for each lookup is independent of the number of elements stored in the table.
## Many hash table designs also allow arbitrary insertions and deletions of key-value pairs, at (amortized) constant average cost per operation.



# try, except statements
while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "Not a valid number.  Try again..."

# Try, except statement with else and finally.
import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()
    finally:
        print "executing finally clause"



# continue
# The continue statement continues to the next iteration of the loop.
# This can reduce the need for additional control statements (if/elif/else),
# further nesting, and make code easier to read.

for (bucket_name, endpoint) in buckets_and_endpoints.items():
   #CODE BLOCK REMOVED

   if self.unwhitelist:
       self.delete_ip_whitelist(bucket_name)
       continue

   bucket = endpoint_connections[endpoint].get_bucket(bucket_name)
   if bucket.name != bucket_name:
       log_line = {'timestamp': time.time(),
                   'account': account_id,
                   'req_bucket': bucket_name,
                   'rx_bucket': bucket.name,
                   'message': 'Bucket names do not match. Skipping'}
       logger.info(json.dumps(log_line))
       continue

   #CODE BLOCK REMOVED


# copy
# Python creates a new object when the contents of a shallow copy are changed.
# The comparisons are value comparisons.
import copy
b = {1: [1,2,3]}

# Reference assignment (same object, same sub-objects)
a = b
id(a) # 4340438192
id(b) # 4340438192
id(a[1]) # 4340522520
id(b[1]) # 4340522520
a == b # True

# Shallow copy (new object, same sub-objects)
a = b.copy()
id(a) # 4340575600
id(b) # 4340438192
id(a[1]) # 4340522520
id(b[1]) # 4340522520
a == b # True
# This creates a new sub-object under 'a'.
a[1] = [4, 5, 6]
id(a[1]) # 4369444592
id(b[1]) # 4340522520
a == b # False
b[1] = [4, 5, 6]
a == b # True

# Deep copy (new object, new sub-objects)
a = copy.deepcopy(b)
a == b # True
id(a) # 4340489584
id(b) # 4340438192
id(a[1]) # 4340168608
id(b[1]) # 4340522520
a == b # True



# Raise a runtime error:
raise RuntimeError('test for validate_request_parameters debug log')



# Lambda function/expressions:

# Combine first and last name into a single "Full Name":
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print full_name("  leonhard", "EULER")
# Leonhard Euler

# Sort list by last name:
scifi_authors = ["Isaac Asimov", "Ray Bradbury", "H. G. Wells"]

# Help on built-in function sort:
help(scifi_authors.sort)
# sort(...) method of builtins.list instance
#     L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print scifi_authors
# ['Isaac Asimov', 'Ray Bradbury', 'H. G. Wells']

# Quadratic function:
def build_quadric_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadric_function(2, 3, -5)
print f(2)
# 9

print build_quadric_function(3, 0, 1)(2)  # 3x^2+1 evaluated for x=2
# 13



# args and kwargs
# Both allow you to pass a variable number of arguments to a function.
# **kwargs allows you to pass keyworded variable length of arguments to a function.

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')
# ('first normal arg:', 'yasoob')
# ('another arg through *argv:', 'python')
# ('another arg through *argv:', 'eggs')
# ('another arg through *argv:', 'test')

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="yasoob")
# name = yasoob
