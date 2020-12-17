# Connect to a Cassandra database, run a query, and print all rows.
from cassandra import ReadTimeout, WriteTimeout
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
import sys
import time
from creds import *
# Put username and password in creds.py

table1 = "storage_account_operations_" + time.strftime('%Y%m')
table2 = "storage_account_delta_usage_" + time.strftime('%Y%m')

endpoints = ['127.0.0.1']
keyspace = 'Metrics'

auth_provider = PlainTextAuthProvider(username=username,
                                      password=password)
cluster = Cluster(endpoints, auth_provider=auth_provider)
session = cluster.connect()
session.set_keyspace(keyspace.lower())

STORAGE_LOCATION_USAGE_TABLE = 'storage_location_usage'
account = 'account_one'
location = 'location_one'
timestamp = 1475186400000

# query = ("SELECT * "
#         "FROM {0} "
#         "WHERE storage_entity_id = %s AND storage_location_id = %s "
#         "AND timestamp = %s;".format(STORAGE_LOCATION_USAGE_TABLE))
# rows = session.execute(query, (account, location, timestamp,))

# query = ("SELECT table_name "
#         "FROM system_schema.tables;")

query = ("SELECT table_name "
         "FROM system_schema.tables "
         "WHERE table_name='storage_account_delta_usage_201805' "
         "ALLOW FILTERING;")

rows = session.execute(query)

print type(ReadTimeout.message)

for row in rows:
  print row

session.shutdown() #testing
sys.exit() #testing

if not rows:
    print "None"
else:
    for row in rows:
        print row.storage_entity_id, row.storage_location_id, row.timestamp, \
        row.bytes_used, row.container_count, row.last_operation_time, \
        row.object_count

session.shutdown()
