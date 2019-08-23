# r is for 'raw string', \w is for 'word character'

import re
string1 = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', string1)
print match.group()
# word:cat

import re
string2 = 'apple\\orange'
match = re.search(r'\\', string2)
print match.group()
# \
