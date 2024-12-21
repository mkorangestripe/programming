# Monte Carlo Yahtzee Simulation

### Coin flips

Permutations and probabilities of coin flips:

```
H, T                                    1/2 (either side)
HH, HT, TT, TH                          1/4 (any pair)
HHH, HHT, HTH, HTT, THT, TTH, TTT, THH  1/8 (any triplet)
```

Combinations and probabilities of three groups of three flips:  

```
Permutations:
{H,H,H} = 1/2 * 1/2 * 1/2 = 1/8
{H,H,T} = 1/2 * 1/2 * 1/2 = 1/8
{H,T,H} = 1/2 * 1/2 * 1/2 = 1/8

Combinations:
{H,H,T}, {H,T,H}, {H,H,H} = 1/8 + 1/8 + 1/8 = 3/8
```

### Dice rolls

Permutations of two dice:

```
{1,1}, {1,2}, {1,3}, {1,4}, {1,5}, {1,6}
{2,1}  {2,2}                       {2,6}
{3,1}         {3,3}                {3,6}
{4,1}                {4,4}         {4,6}
{5,1}                       {5,5}  {5,6}
{6,1}                              {6,6}
```

Probability of rolling two dice with the same side:

```
6 / (6 * 6) = 1/6 or ~16.67%
```

Probability of rolling Yahtzee (all five dice the same):

```
6 / (6 * 6 * 6 * 6 * 6) = ~0.00077 or 0.077%
```

### Yahtzee

```python
import random

# DICE_ROLLS = 100
# DICE_ROLLS = 100
# DICE_ROLLS = 1000
# DICE_ROLLS = 10_000
# DICE_ROLLS = 100_000
DICE_ROLLS = 1_000_000

def yahtzee(dice_rolls):
    """Monte Carlo simulation"""

    yahtzee_cnt = 0.0
    for _simulation in range(dice_rolls):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        d3 = random.randint(1,6)
        d4 = random.randint(1,6)
        d5 = random.randint(1,6)
        if d1 == d2 == d3 == d4 == d5:
            yahtzee_cnt += 1

    return yahtzee_cnt / dice_rolls

print('Yahtzee simulation...')
print("Dice rolls:", DICE_ROLLS)
print("Probability of five dice the same:", yahtzee(DICE_ROLLS))
```

```
Yahtzee simulation...
Dice rolls: 1000000
Probability of five dice the same: 0.000757
```
