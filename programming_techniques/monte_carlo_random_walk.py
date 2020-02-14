# Random Walk and Monte Carlo simulation
# Examples from Socratica
import random

def random_walk_2(n):
    """
    Return coordinates after 'n' block random walk.
    The tuples in random.choice represent North, South, East, West)
    """
    x,y = 0,0
    for i in range(n):
        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return(x,y)


# To test random_walk2()
# With a walk length of 25, the furthest distance would be (+-5,+-5)
# The the closest would be (0,0)
number_of_walks = 25
for i in range(number_of_walks):
    walk = random_walk_2(10)
    print(walk, "Distance from home = ",
          abs(walk[0]) + abs(walk[1]))
print


# What is the longest random walk you
# can take so that on average you will
# end up 4 blocks or fewer from home?
# Using the Monte Carlo method...

number_of_walks = 10000
# number_of_walks = 20000

# Monte Carlo simulation
for walk_length in range(1,31):
    no_transport = 0  # number of walks 4 or fewer blocks from home
    for i in range(number_of_walks):
        (x,y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance <=4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print "Walk size = ", walk_length,\
          " / % of no transport = ", 100*no_transport_percentage

# Walk size =  1  / % of no transport =  100.0
# Walk size =  2  / % of no transport =  100.0
# Walk size =  3  / % of no transport =  100.0
# Walk size =  4  / % of no transport =  100.0
# Walk size =  5  / % of no transport =  88.25
# Walk size =  6  / % of no transport =  94.04
# Walk size =  7  / % of no transport =  76.28
# Walk size =  8  / % of no transport =  86.06
# Walk size =  9  / % of no transport =  67.18
# Walk size =  10  / % of no transport =  79.37
# Walk size =  11  / % of no transport =  60.47
# Walk size =  12  / % of no transport =  73.29
# Walk size =  13  / % of no transport =  52.73
# Walk size =  14  / % of no transport =  66.71
# Walk size =  15  / % of no transport =  49.28
# Walk size =  16  / % of no transport =  62.55
# Walk size =  17  / % of no transport =  44.56
# Walk size =  18  / % of no transport =  58.24
# Walk size =  19  / % of no transport =  41.0
# Walk size =  20  / % of no transport =  54.63
# Walk size =  21  / % of no transport =  37.31
# Walk size =  22  / % of no transport =  51.08
# Walk size =  23  / % of no transport =  35.87
# Walk size =  24  / % of no transport =  48.13
# Walk size =  25  / % of no transport =  33.54
# Walk size =  26  / % of no transport =  45.48
# Walk size =  27  / % of no transport =  30.71
# Walk size =  28  / % of no transport =  42.18
# Walk size =  29  / % of no transport =  28.97
# Walk size =  30  / % of no transport =  40.64

# The longest walk with over 50% change of no transport is 22 blocks.
