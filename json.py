# Connect to and authenticate with a Zabbix server using a json string.
# Parts of the script below are time sensitive.
# This fails when run line by line.
import json
import httplib

output_to_json = {"jsonrpc": "2.0",
                  "method":"user.login",
                  "params": {"user":"xxxxxx",
                             "password":"xxxxxx"},
                  "auth":None,
                  "id":1}

json_string = json.dumps(output_to_json,
                         sort_keys=True,indent=4,
                         separators=(',', ': '))

# Establish connection and authenticate.
headers = {"Content-type":"application/json-rpc"}
conn = httplib.HTTPSConnection("zabbix.dgtlrvr.net", 443)
conn.request("POST","/zabbix/api_jsonrpc.php",json_string,headers)
response = conn.getresponse()

data = response.read()
auth = json.loads(data)
key = auth["result"]

# Submit query.
hostgroup_query = {"jsonrpc": "2.0",
                   "method":"hostgroup.get",
                   "params": {
                       "search":{"name":"Bluehornet"},
                       "output":"extend",
                       "selectHosts":["name"]
                   },
                   "auth": key,
                   "id": 1
}

json_string = json.dumps(hostgroup_query,
                         sort_keys=True,indent=4,
                         separators=(',', ': '))

conn.request("POST","/zabbix/api_jsonrpc.php",json_string,headers)
response = conn.getresponse()
data = response.read()

# Parse returned data.
parsed_data = json.loads(data)
for group in parsed_data['result']:
    print '##  ' + group['name']
    for host in group['hosts']:
                    print host['name']
    print
