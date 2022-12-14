#!/usr/bin/env python

"""
Random Walk and Monte Carlo simulation
Examples from Socratica
"""

import random

def random_walk_2(n):
    """
    Return coordinates after 'n' block random walk.
    The tuples in random.choice represent North, South, East, West)
    """
    x,y = 0,0
    for _i in range(n):
        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return(x,y)


# To test random_walk2()
# With a walk length of 25, the furthest distance would be (+-5,+-5)
# The the closest would be (0,0)
NUMBER_OF_WALKS = 25
for i in range(NUMBER_OF_WALKS):
    walk = random_walk_2(10)
    print(walk, "Distance from home = ",
          abs(walk[0]) + abs(walk[1]))
print('')


# What is the longest random walk you
# can take so that on average you will
# end up 4 blocks or fewer from home?
# Using the Monte Carlo method...

NUMBER_OF_WALKS = 10000
# NUMBER_OF_WALKS = 20000

# Monte Carlo simulation
for walk_length in range(1,31):
    NO_TRANSPORT = 0  # number of walks 4 or fewer blocks from home
    for i in range(NUMBER_OF_WALKS):
        (x,y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            NO_TRANSPORT += 1
    no_transport_percentage = float(NO_TRANSPORT) / NUMBER_OF_WALKS
    print("Walk size =", walk_length,\
          "-- Probability of no transport =", round(100 * no_transport_percentage, 2),"%")

# Walk size = 1 -- Probability of no transport = 100.0 %
# Walk size = 2 -- Probability of no transport = 100.0 %
# Walk size = 3 -- Probability of no transport = 100.0 %
# Walk size = 4 -- Probability of no transport = 100.0 %
# Walk size = 5 -- Probability of no transport = 87.82 %
# Walk size = 6 -- Probability of no transport = 94.17 %
# Walk size = 7 -- Probability of no transport = 75.55 %
# Walk size = 8 -- Probability of no transport = 86.06 %
# Walk size = 9 -- Probability of no transport = 67.71 %
# Walk size = 10 -- Probability of no transport = 78.88 %
# Walk size = 11 -- Probability of no transport = 60.35 %
# Walk size = 12 -- Probability of no transport = 72.89 %
# Walk size = 13 -- Probability of no transport = 52.8 %
# Walk size = 14 -- Probability of no transport = 67.23 %
# Walk size = 15 -- Probability of no transport = 48.5 %
# Walk size = 16 -- Probability of no transport = 62.5 %
# Walk size = 17 -- Probability of no transport = 43.64 %
# Walk size = 18 -- Probability of no transport = 57.35 %
# Walk size = 19 -- Probability of no transport = 41.89 %
# Walk size = 20 -- Probability of no transport = 55.34 %
# Walk size = 21 -- Probability of no transport = 37.51 %
# Walk size = 22 -- Probability of no transport = 50.47 %
# Walk size = 23 -- Probability of no transport = 35.57 %
# Walk size = 24 -- Probability of no transport = 48.26 %
# Walk size = 25 -- Probability of no transport = 32.71 %
# Walk size = 26 -- Probability of no transport = 45.19 %
# Walk size = 27 -- Probability of no transport = 30.99 %
# Walk size = 28 -- Probability of no transport = 44.09 %
# Walk size = 29 -- Probability of no transport = 29.61 %
# Walk size = 30 -- Probability of no transport = 41.61 %

# The longest walk with over 50% chance of no transport is 22 blocks.
