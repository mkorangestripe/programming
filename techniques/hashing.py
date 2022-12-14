#!/usr/bin/env python
"""
Send a password using hashing.
"""

import hashlib
import random
import string

print("Server1")
NUMBERS_LETTERS = string.digits + string.ascii_letters
RANDOM_STRING = ''.join(random.sample(NUMBERS_LETTERS,  8))
HASH = hashlib.sha1(RANDOM_STRING.encode('utf-8')).hexdigest()
HASHPASS = HASH[-10:-2] # To limit the password to an arbitrary 8 characters.
print("Random string:", RANDOM_STRING)
print("hash:", HASH)
print("hashpass:", HASHPASS)
print("Set the local user's password to hashpass.")
print("Send the random string to Client1.\n")

print("Client1")
# randomString is the random string from Server1
HASH = hashlib.sha1(RANDOM_STRING.encode('utf-8')).hexdigest()
HASHPASS = HASH[-10:-2]
print("Random string:", RANDOM_STRING)
print("hash:", HASH)
print("hashpass:", HASHPASS)
print("Login to Server1 using hashpass as the password.")
