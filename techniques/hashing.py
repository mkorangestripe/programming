#!/usr/bin/env python
# Send a password with some security using hashing.

print("Server1")
import string, random, hashlib
numbers_letters = string.digits + string.ascii_letters
randomString = ''.join(random.sample(numbers_letters,  8))
hash = hashlib.sha1(randomString.encode('utf-8')).hexdigest()
hashpass = hash[-10:-2] # To limit the password to an arbitrary 8 characters.
print("Random string:", randomString)
print("hash:", hash)
print("hashpass:", hashpass)
print("Set the local user's password to hashpass.")
print("Send the random string to Client1.\n")

print("Client1")
import hashlib
# randomString is the random string from Server1
hash = hashlib.sha1(randomString.encode('utf-8')).hexdigest()
hashpass = hash[-10:-2]
print("Random string:", randomString)
print("hash:", hash)
print("hashpass:", hashpass)
print("Login to Server1 using hashpass as the password.")
