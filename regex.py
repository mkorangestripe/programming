import re


# r is 'raw string', \w is 'word character'

string1 = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', string1)
match.group() # word:cat

string2 = 'apple\\orange'
match = re.search(r'\\', string2)
match.group() # \


# Search examples

line1 = '    app_id: bc7a46ad-214d-4845-8771-fbe43670890a'
line2 = '    app_id: bc7a46ad00-214d-4845-8771-fbe43670890aa'
line3 = '   "id": "57547f91-fbf2-4512-9945-6f8ba488e63f",'

re_uuid = re.compile("[0-F]{8}-([0-F]{4}-){3}[0-F]{12}", re.I) # True for line2, but works for uuid's in quotes
re_uuid = re.compile("[0-F]{8}-([0-F]{4}-){3}[0-F]{12}\Z", re.I) # False if uuid in quotes
match = re_uuid.search(line1)
bool(match)
match.group()


# Match examples

s1 = '611bbd7b-bd31-4ad0-8293-e8414bcb3053'
s2 = '611bbd7b-bd31-4ad0-8293-e8414bcb3053 '
s3 = ' 611bbd7b-bd31-4ad0-8293-e8414bcb3053'

re_uuid = re.compile("[0-F]{8}-([0-F]{4}-){3}[0-F]{12}", re.I)
match = re_uuid.match(s1) # True
match = re_uuid.match(s2) # True
match = re_uuid.match(s3) # False
bool(match)
match.group()
