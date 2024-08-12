#!/usr/bin/env python
"""
Find all derangements of a number list.
This is all permutations where each position is different from the original.

Example list:
[0, 1, 2, 3]

Possible numbers in each position (length - 1):
[1,2,3], [0,2,3], [0,1,3], [0,1,2]

Permutations:
[1, 0, 3, 2]
[1, 2, 3, 0]
[1, 3, 0, 2]

[2, 0, 3, 1]
[2, 3, 0, 1]
[2, 3, 1, 0]

[3, 0, 1, 2]
[3, 2, 0, 1]
[3, 2, 1, 0]
"""

# NUMBER_LIST = [0, 1]
# NUMBER_LIST = [0, 1, 2]
NUMBER_LIST = [0, 1, 2, 3]

valid_options = []
for i in range(len(NUMBER_LIST)):
    sub_list = NUMBER_LIST.copy()
    del sub_list[i]
    valid_options.append(sub_list)

# print(valid_options)

for first_number in (valid_options[0]):
    print(str(first_number) + " " + "first number")
    print()
    valid_perms = [first_number]
    for sublist in valid_options[1:]:
        # print(sublist)
        for number in sublist:
            if number not in valid_perms:
                valid_perms.append(number)
                print(valid_perms)
                break
        print()
