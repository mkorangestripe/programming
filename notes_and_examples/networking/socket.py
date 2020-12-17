# socket

# Get the ssh header.
# This is similar to curl 192.168.1.112:22
import socket
s = socket.socket()
s.connect(('192.168.1.112', 22))
print s.recv(200) # SSH-2.0-OpenSSH_5.3


# Get the first 300 bytes of the HTTP server's response using the HEAD method.
# This is similar to: curl -I 192.168.1.112
import socket
s = socket.socket()
s.connect(('192.168.1.112', 80))
s.send("HEAD / HTTP/1.0\r\n\r\n")
for line in s.recv(300).split('\r\n'):
    print line
# This outputs the following...

# HTTP/1.1 200 OK
# Date: Fri, 01 Mar 2019 19:58:37 GMT
# Server: Apache/2.2.15 (CentOS)
# Last-Modified: Fri, 13 Jun 2014 20:12:05 GMT
# ETag: "40b48-29a-4fbbd4a902c8f"
# Accept-Ranges: bytes
# Content-Length: 666
# Connection: close
# Content-Type: text/html; charset=UTF-8


# Check if a port is open.
# This is similar to nc -z 192.168.1.112 80
import socket
address = '192.168.1.112'
port = 80
s = socket.socket()
try:
    s.connect((address, port))
    print "Connected to %s on port %s" % (address, port)
except socket.error, e:
    print "Connection to %s on port %s failed: %s" % (address, port, e)
# This outputs the following...
# Connected to 192.168.1.112 on port 80
