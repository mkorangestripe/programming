# Examples of running unittests:
# python ps6_test.py (This outputs the individual test results)
# python -m unittest ps6_test  (This outputs only the combined results)
# python -m unittest (This runs all unittests in the directory)

# Simple example of a unittest.
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
   unittest.main()



# requests and requests_mock

import requests
import requests_mock

# Simple example of requests_mock.
with requests_mock.Mocker() as m:
    m.get('http://test.com', text='hello1')
    print requests.get('http://test.com').text


# Example of requests_mock as a decorator.
@requests_mock.Mocker()
def test_function(m):
    m.get('http://test.com', text='hello2')
    return requests.get('http://test.com').text

print test_function()



# Unittest using mock and requests_mock.

import json
import unittest
import mock
import requests_mock

from objectstorage_billing.common.cleversafe_account_deleter import\
    CleversafeAccountDeleter

DELETER_PATH = 'objectstorage_billing.common.cleversafe_account_deleter'

class TestCleversafeAccountDeleter(unittest.TestCase):

    def setUp(self):
        self.endpoint = '127.0.0.1'
        self.port = '8338'
        self.username = 'name'
        self.password = 'pass'
        self.endpoints = {}
        self.deleter = CleversafeAccountDeleter(self.endpoint,
                                                self.port,
                                                self.username,
                                                self.password,
                                                self.endpoints)

    def test_attempt_account_deletion(self):
        url = 'https://{0}:{1}/accounts/{2}'.format(self.endpoint,
                                                    self.port,
                                                    self.account_id)

       with requests_mock.Mocker() as m, \
            mock.patch(DELETER_PATH + '.logger') as log_mock:
        m.delete(url, status_code=204, text='{}')
        self.deleter.attempt_account_deletion(self.account_id)
        self.assertEqual(log_mock.warning.called, False)

    def test_delete_ip_whitelist(self):
        bucket_name = "ipwhitelist-testbucket"

        bucket_info = {"storage_location": "xxxxx",
                       "name": bucket_name,
                       "service_instance": "107",
                       "acl": {"xxxxx": ["full"]},
                       "retention_policy": "NONE",
                       "hard_quota": 0,
                       "firewall": {"format": 1, "allowed_ip": \
                           ["192.168.1.14", "192.168.1.15"]},
                       "time_created": "2019-02-21T16:37:05.383Z",
                       "time_updated": "2019-03-07T22:23:30.525Z"}

        url = 'https://{0}:{1}/container/{2}'.format(
            self.endpoint,
            self.port,
            bucket_name)

        with requests_mock.Mocker() as m:
            m.get(url, status_code=200, text=json.dumps(bucket_info))
            m.patch(url, status_code=200, text=json.dumps(bucket_info))
            self.deleter.delete_ip_whitelist(bucket_name)
            self.assertEqual(
                json.loads(m.last_request.text),
                {
                      "firewall": {
                          "allowed_ip": []
                      }
                })

if __name__ == '__main__':
   unittest.main()
