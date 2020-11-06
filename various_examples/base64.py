import base64

# base64 encoding for python 3

passwd = ''
encoded = base64.b64encode(passwd.encode('utf-8'))
print(encoded)

encoded_pw = b''
decoded = base64.b64decode(encoded_pw).decode('utf-8')
print(decoded)
