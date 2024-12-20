### Send a password using hashing

Server

```python
import hashlib
import random
import string

NUMBERS_LETTERS = string.digits + string.ascii_letters
RANDOM_STRING = ''.join(random.sample(NUMBERS_LETTERS,  8))
HASH = hashlib.sha1(RANDOM_STRING.encode('utf-8')).hexdigest()
HASHPASS = HASH[-10:-2]  # limit the password to an arbitrary 8 characters

print("Random string:", RANDOM_STRING)
print("hash:", HASH)
print("hashpass:", HASHPASS)
print("Set the local user's password to hashpass.")
print("Send the random string to the client.")
```

```
Random string: 5l0xrscn
hash: 37c470647e215d4b3e00ff7c0949a996513ebd45
hashpass: 96513ebd
Set the local user's password to hashpass.
Send the random string to the client.
```

Client

```python
import hashlib

RANDOM_STRING = '5l0xrscn'  # from the server
HASH = hashlib.sha1(RANDOM_STRING.encode('utf-8')).hexdigest()
HASHPASS = HASH[-10:-2]

print("Random string:", RANDOM_STRING)
print("hash:", HASH)
print("hashpass:", HASHPASS)
print("Login to the server using hashpass as the password.")
```

```
Random string: 5l0xrscn
hash: 37c470647e215d4b3e00ff7c0949a996513ebd45
hashpass: 96513ebd
Login to the server using hashpass as the password.
```
