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
