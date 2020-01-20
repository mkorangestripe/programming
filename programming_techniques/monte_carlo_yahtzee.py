import random

# Coin flip probability examples:
# H, T - 1/2 (either side)
# HH, HT, TT, TH - 1/4 (any pair)
# HHH, HHT, HTH, HTT, THT, TTT, TTH, THH - 1/8 (any pair)

# Probabilities of three flips and three groups of three flips.
# The order of the groups does not matter.
# {H,H,H} 1/2 * 1/2 * 1/2 = 1/8
# {H,T,H} 1/2 * 1/2 * 1/2 = 1/8
# {H,H,H}, {H,T,H}, {T,H,H} 1/8 + 1/8 + 1/8 = 3/8

# Dice, possible pairs:
# {1,1}, {1,2}, {1,3}, {1,4}, {1,5}, {1,6}
# {2,1}  {2,2}                       {2,6}
# {3,1}         {3,3}                {3,6}
# {4,1}                {4,4}         {4,6}
# {5,1}                       {5,5}  {5,6}
# {6,1}                              {6,6}

# Probability of rolling two dice the same as show above.
# 6 / (6 * 6) = 1/6 or ~16.67%

# Probability of rolling Yahtzee:
# 6 / (6 * 6 * 6 * 6 * 6) = ~0.00077 or 0.077%

# Monte Carlo simulation
def yahtzee(dice_rolls):
    yahtzee_cnt = 0.0
    for simulation in range(dice_rolls):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        d3 = random.randint(1,6)
        d4 = random.randint(1,6)
        d5 = random.randint(1,6)
        if d1 == d2 == d3 == d4 == d5:
            yahtzee_cnt += 1
    return (yahtzee_cnt / dice_rolls)

# With 1,000,000 dice rolls, the average is about 0.00075 or 0.075%
# This is the probability that all five dice will be the same.

# dice_rolls = 100
# dice_rolls = 100
# dice_rolls = 1000
# dice_rolls = 10000
# dice_rolls = 100000
dice_rolls = 1000000

print 'Yahtzee simulation...'
print yahtzee(dice_rolls)
# Yahtzee simulation...
# 0.000762
