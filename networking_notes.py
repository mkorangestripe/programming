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



# httplib

# Get http status code.
import httplib
conn = httplib.HTTPConnection("192.168.1.112")
# conn.request("GET", "/index.html")
conn.request("GET", "/")
r1 = conn.getresponse()
print r1.status, r1.reason


# Get http status code, with some error checking.
import httplib
resource = 'store/games'
resource = '/' + resource
address = '192.168.1.112'
port = 7775
try:
    conn = httplib.HTTPConnection(address, port)
    print 'HTTP connection created successfully'
    req = conn.request('GET', resource)
    print 'request for %s successful' % resource
    response = conn.getresponse()
    print 'response status: %s' % response.status
except socket.error, e:
    print 'HTTP connection failed: %s' % e
finally:
    conn.close()
    print 'HTTP connection closed successfully'



# urllib
import urllib
# This is similar to: wget 192.168.1.112
url = 'http://192.168.1.112'
filename = 'index.html'
urllib.urlretrieve(url, filename)

# urllib2
import urllib2
# This gets the first 100 bytes of content:
# This is similar to curl -r 0-99 192.168.1.112
f = urllib2.urlopen('http://192.168.1.112')
print f.read(100)



# requests
import requests
url = 'http://192.168.1.112'
# response = requests.get(url)
response = requests.get(url,
                        auth=(username, password),
                        verify=True)
content = response.content



# pycurl
import pycurl
# This is similar to: curl 192.168.1.112
c = pycurl.Curl()
c.setopt(c.URL, '192.168.1.112')
c.perform()



# SimpleHTTPServer
# This will serve the current directory or index.html in the current directory on port 8000.
# python -m SimpleHTTPServer 8000



# SSH (paramiko)

# SSH simple example.
import paramiko
hostname = '192.168.1.111'
port = 22
username = 'gp'
password = 'xxxxxxxx'
if __name__ == "__main__":
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('/sbin/ifconfig')
    print stdout.read()
    s.close()


# SSH example without password.
# This requires a key file that was created with an empty passphrase.
# If the key was created with a passphrase...
# run ssh-agent and ssh-add beforehand.
import paramiko
hostname = '192.168.1.111'
port = 22
username = 'gp'
pkey_file = '/home/gp/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pkey_file)
s = paramiko.SSHClient()
s.load_system_host_keys()
s.connect(hostname, port, username, pkey=key)
stdin, stdout, stderr = s.exec_command('/sbin/ifconfig')
print stdout.read()
s.close()


# SFTP example.
import paramiko
dir_path = '/home/username/pytmp'
if __name__ == "__main__":
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for f in files:
        print 'Retrieving', f
        sftp.get(os.path.join(dir_path, f), f)
    t.close()



# snmp
import netsnmp
oid = netsnmp.Varbind('sysDescr')
netsnmp.snmpwalk(oid, Version = 2, DestHost = "192.168.1.112", Community = "public")



# Email
import smtplib
from email.mime.text import MIMEText

COMMASPACE = ', '

me = os.environ['USER'] + '@domain.com'
recipients = ['addr1@domain.com', 'addr2@domain.com']

body = 'This is a test from Python smtplib.'
msg = MIMEText(body)

msg['Subject'] = 'Test from Python smtplib'
msg['From'] = me
msg['To'] = COMMASPACE.join(recipients)

s = smtplib.SMTP('localhost')
s.sendmail(me, recipients, msg.as_string())
s.quit()
