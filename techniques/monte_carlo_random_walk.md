# Monte Carlo Random Walk

### Random Walk

```python
import random

def random_walk(n_blocks):
    """
    Return coordinates after a random walk.
    The tuples in random.choice represent North, South, East, West.
    """

    x,y = 0,0
    for _i in range(n_blocks):
        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy

    return(x,y)
```

```python
BLOCKS = 10
WALKS = 25

for i in range(WALKS):
    walk = random_walk(BLOCKS)
    print(walk, "Distance from home =", abs(walk[0]) + abs(walk[1]))
```

```
(0, 0) Distance from home = 0
(3, -3) Distance from home = 6
(1, -1) Distance from home = 2
(-1, 5) Distance from home = 6
(1, 1) Distance from home = 2
(-3, -3) Distance from home = 6
(-2, 0) Distance from home = 2
(-2, 4) Distance from home = 6
(1, -1) Distance from home = 2
(1, -1) Distance from home = 2
(-2, -2) Distance from home = 4
(-1, -1) Distance from home = 2
(4, 0) Distance from home = 4
(-2, -2) Distance from home = 4
(1, 1) Distance from home = 2
(-1, -1) Distance from home = 2
(-2, 2) Distance from home = 4
(0, 4) Distance from home = 4
(1, 3) Distance from home = 4
(-3, 1) Distance from home = 4
(-1, 3) Distance from home = 4
(-8, -2) Distance from home = 10
(3, 5) Distance from home = 8
(1, -1) Distance from home = 2
(-4, -2) Distance from home = 6
```

### Monte Carlo Simulation

```python
# This finds the longest random walk possible ending within a distance where no transport is required.

NO_TRANSPORT_DIST = 4
WALK_LEN_UPPER_LIM = 31
NUMBER_OF_WALKS = 10000
# NUMBER_OF_WALKS = 20000

for walk_length in range(1, WALK_LEN_UPPER_LIM):
    END_WITHIN_NT_DIST = 0

    for i in range(NUMBER_OF_WALKS):
        (X,Y) = random_walk(walk_length)
        distance = abs(X) + abs(Y)
        if distance <= NO_TRANSPORT_DIST:
            END_WITHIN_NT_DIST += 1

    no_transport_percentage = float(END_WITHIN_NT_DIST) / NUMBER_OF_WALKS
    print("Walk length =", walk_length,\
          "-- Probability of no transport =", str(round(100 * no_transport_percentage, 2)) + "%")
```

```
Walk length = 1 -- Probability of no transport = 100.0%
Walk length = 2 -- Probability of no transport = 100.0%
Walk length = 3 -- Probability of no transport = 100.0%
Walk length = 4 -- Probability of no transport = 100.0%
Walk length = 5 -- Probability of no transport = 88.01%
Walk length = 6 -- Probability of no transport = 93.58%
Walk length = 7 -- Probability of no transport = 76.56%
Walk length = 8 -- Probability of no transport = 85.78%
Walk length = 9 -- Probability of no transport = 67.22%
Walk length = 10 -- Probability of no transport = 80.0%
Walk length = 11 -- Probability of no transport = 59.14%
Walk length = 12 -- Probability of no transport = 73.07%
Walk length = 13 -- Probability of no transport = 53.59%
Walk length = 14 -- Probability of no transport = 66.86%
Walk length = 15 -- Probability of no transport = 48.85%
Walk length = 16 -- Probability of no transport = 62.12%
Walk length = 17 -- Probability of no transport = 43.73%
Walk length = 18 -- Probability of no transport = 58.2%
Walk length = 19 -- Probability of no transport = 41.01%
Walk length = 20 -- Probability of no transport = 53.68%
Walk length = 21 -- Probability of no transport = 37.96%
Walk length = 22 -- Probability of no transport = 50.55%
Walk length = 23 -- Probability of no transport = 35.28%
Walk length = 24 -- Probability of no transport = 48.44%
Walk length = 25 -- Probability of no transport = 33.55%
Walk length = 26 -- Probability of no transport = 43.67%
Walk length = 27 -- Probability of no transport = 30.94%
Walk length = 28 -- Probability of no transport = 43.71%
Walk length = 29 -- Probability of no transport = 30.23%
Walk length = 30 -- Probability of no transport = 41.24%
```

The longest walk with over 50% probability of no transport needed is 22 blocks.
