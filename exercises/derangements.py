#!/usr/bin/env python
"""
Find all derangements of a number list.
This is all permutations where each position is different from the original.
This method generates the permutations randomly and works for small lists,
but is not the most efficient solution.

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

import random

# NUMBER_LIST = [0, 1]
# NUMBER_LIST = [0, 1, 2]
NUMBER_LIST = [0, 1, 2, 3]

RANDOM_SHUFFLE_MULTIPLIER = 100

def list_is_valid(random_number_list):
    """Check whether all positions are different from the original list"""
    valid_permutation = True
    for i in range(len(random_number_list)):
        if random_number_list[i] == NUMBER_LIST[i]:
            valid_permutation = False
            break
    return valid_permutation

NUM_LIST_LEN = len(NUMBER_LIST)
number_list_random = NUMBER_LIST.copy()
valid_permutations = []

for shuffles in range(NUM_LIST_LEN * RANDOM_SHUFFLE_MULTIPLIER):
    random.shuffle(number_list_random)
    if number_list_random not in valid_permutations\
    and list_is_valid(number_list_random):
        valid_permutations.append(number_list_random.copy())
    # print(valid_permutations)
    # print()

print(valid_permutations)
