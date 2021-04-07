#!/usr/bin/env python
# Hashing
# http://en.wikipedia.org/wiki/Hash_function
# A hash function is any algorithm that maps data of variable length to data of a fixed length.
# The values returned by a hash function are called hash values, hash codes, hash sums, checksums or simply hashes.
# Hash functions are primarily used in hash tables, to quickly locate a data record.
# http://en.wikipedia.org/wiki/Hash_table
# In a well-dimensioned hash table, the average cost (number of instructions) for each lookup is independent of the number of elements stored in the table.
# Many hash table designs also allow arbitrary insertions and deletions of key-value pairs, at (amortized) constant average cost per operation.


# Send a password with some security using hashing.

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
