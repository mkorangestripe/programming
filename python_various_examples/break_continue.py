# The continue statement continues to the next iteration of the loop.
# This can reduce the need for additional control statements (if/elif/else),
# further nesting, and make code easier to read.

for (bucket_name, endpoint) in buckets_and_endpoints.items():
   #CODE BLOCK REMOVED

   if self.unwhitelist:
       self.delete_ip_whitelist(bucket_name)
       continue

   bucket = endpoint_connections[endpoint].get_bucket(bucket_name)
   if bucket.name != bucket_name:
       log_line = {'timestamp': time.time(),
                   'account': account_id,
                   'req_bucket': bucket_name,
                   'rx_bucket': bucket.name,
                   'message': 'Bucket names do not match. Skipping'}
       logger.info(json.dumps(log_line))
       continue

   #CODE BLOCK REMOVED
