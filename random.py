import random

# Random float x, 0.0 <= x < 1.0
random.random() # 0.9077696509551497

# Random float x, 1.0 <= x < 10.0
random.uniform(1, 10) # 6.38304208099131

# Integer from 1 to 10, endpoints included
random.randint(1, 10) # 7

# Integer from 0 to 359
random.randrange(360) # 119

# Even integer from 0 to 100
random.randrange(0, 101, 2) # 70

# Choose a random element
random.choice('abcdefghij') # h

# Choose 3 elements
items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
# [7, 3, 5, 2, 1, 4, 6]
random.sample([1, 2, 3, 4, 5],  3)
# [5, 3, 2]
