#!/usr/bin/env python

"""
0/1 Knapsack problem
Examples from MIT OCW
"""

import random

# Brute force algorithm of generating all combinations might take too long.
# Greedy algorithm doesn't always yield the best solution and doesn't show how close the approximation is.
# Here's a greedy algorithm using calories as a limiting factor.
# The results are computed by value, calories, or the ratio of value/calories.
# In this example 'greedy by value' produced the highest total value <= the calorie limit.

class Food:
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'

def buildMenu(names, values, calories):
    """names, values, calories lists of same length.
       name a list of strings
       values and calories lists of numbers
       returns list of Foods"""
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu

def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost >= 0,
         keyFunction maps elements of items to numbers"""
    itemsCopy = sorted(items, key = keyFunction,
                       reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)

def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits,
               lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.density)


names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 1000)

# Use greedy by value to allocate 1000 calories
# Total value of items taken = 424.0
#     burger: <100, 354>
#     pizza: <95, 258>
#     beer: <90, 154>
#     wine: <89, 123>
#     apple: <50, 95>

# Use greedy by cost to allocate 1000 calories
# Total value of items taken = 413.0
#     apple: <50, 95>
#     wine: <89, 123>
#     cola: <79, 150>
#     beer: <90, 154>
#     donut: <10, 195>
#     pizza: <95, 258>

# Use greedy by density to allocate 1000 calories
# Total value of items taken = 413.0
#     wine: <89, 123>
#     beer: <90, 154>
#     cola: <79, 150>
#     apple: <50, 95>
#     pizza: <95, 258>
#     donut: <10, 195>



# This is an example of the 0/1 knapsack problem using memoization
# to reduce the redundancy.

def buildLargeMenu(numItems, maxVal, maxCost):
    """
    Return a list of food items (as objects) with random value and caloric cost
    """
    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items


def fastMaxVal(toConsider, avail, memo={}):
    """Assumes toConsider a list of subjects, avail a weight
         memo supplied by recursive calls
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the subjects of that solution"""
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0: # check whether food item list is empty or remaining calories is 0
        result = (0, ())
    elif toConsider[0].getCost() > avail: # check whether food item 0 has more calories than remaining calories
        # Explore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = \
            fastMaxVal(toConsider[1:],
                       avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
                                               avail, memo)
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result


# Example of fastMaxVal()

# items:
# item, value, calories
# 0: <20, 9>
# 1: <73, 62>
# 2: <81, 182>
# 3: <81, 43>
# 4: <31, 199>
# 5: <17, 14>
# 6: <85, 139>
# 7: <67, 115>
# 8: <64, 145>
# 9: <45, 137>

# Start down the left branch...
# fastMaxVal(items, 750)
# nextItem = '0: <20, 9>'
# withVal, withToTake = fastMaxVal(items[1:], 741, memo)
# nextItem = '1: <73, 62>'
# withVal, withToTake = fastMaxVal(items[1:], 679, memo)
# nextItem = '2: <81, 182>'
# withVal, withToTake = fastMaxVal(items[1:], 497, memo)
# nextItem = '4: <31, 199>'
# withVal, withToTake = fastMaxVal(items[1:], 454, memo)
# nextItem = '5: <17, 14>'
# withVal, withToTake = fastMaxVal(items[1:], 255, memo)
# nextItem = '6: <85, 139>'
# withVal, withToTake = fastMaxVal(items[1:], 241, memo)
# nextItem = '7: <67, 115>'
# withVal, withToTake = fastMaxVal(items[1:], 102, memo)
# toConsider[0].getCost() > avail: # 115 > 102
# result = fastMaxVal(toConsider[1:], avail, memo) -- This is 'items 8 and 9', 102, memo
# Repeat with only item 8, then only item 9
# toConsider == []
# result = (0, ())
# Step back a few lines...
# withVal, withToTake = 0, ()
# Proceed with next steps...
# withVal += nextItem.getValue() -- This is 0 += 64 = 64
# Now do the same as above with remaing two items, 8 and 9
# This is considered the right branch now
# withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
#                                        avail, memo)
# Then it looks like these two branches are compared for value.
# And the memoization starts to happen.


def testMaxVal(foods, maxUnits, algorithm, printItems=True):
    print('Menu contains', len(foods), 'items')
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = algorithm(foods, maxUnits)
    if printItems:
        print('Total value of items taken =', val)
        for item in taken:
            print('   ', item)

# For each number of food items (numItems), create an items list with
# random value and caloric cost.
# Then determine the combination of food with the largest value
# less than the maximum calories.
for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, fastMaxVal, True)

# Menu contains 5 items
# Use search tree to allocate 750 calories
# Total value of items taken = 141
#     4: <45, 65>
#     3: <2, 98>
#     2: <19, 107>
#     1: <72, 216>
#     0: <3, 221>
# Menu contains 10 items
# Use search tree to allocate 750 calories
# Total value of items taken = 348
#     9: <72, 182>
#     5: <33, 27>
#     4: <69, 105>
#     3: <66, 216>
#     2: <25, 75>
#     1: <44, 59>
#     0: <39, 55>
# Menu contains 15 items
# Use search tree to allocate 750 calories
# Total value of items taken = 427
#     9: <72, 182>
#     5: <33, 27>
#     9: <85, 37>
#     8: <51, 131>
#     5: <46, 110>
#     2: <56, 53>
#     1: <49, 74>
#     0: <35, 105>
# Menu contains 20 items
# Use search tree to allocate 750 calories
# Total value of items taken = 546
#     9: <85, 37>
#     8: <51, 131>
#     7: <52, 120>
#     11: <65, 231>
#     6: <63, 3>
#     5: <86, 34>
#     2: <60, 40>
#     0: <84, 143>
# Menu contains 25 items
# Use search tree to allocate 750 calories
# Total value of items taken = 719
#     9: <72, 182>
#     9: <85, 37>
#     14: <84, 144>
#     11: <57, 47>
#     10: <48, 57>
#     9: <61, 32>
#     7: <59, 70>
#     5: <56, 53>
#     4: <78, 95>
#     1: <29, 24>
#     0: <90, 5>
# Menu contains 30 items
# Use search tree to allocate 750 calories
# Total value of items taken = 719
#     9: <72, 182>
#     9: <85, 37>
#     14: <84, 144>
#     11: <57, 47>
#     10: <48, 57>
#     9: <61, 32>
#     7: <59, 70>
#     5: <56, 53>
#     4: <78, 95>
#     1: <29, 24>
#     0: <90, 5>
# Menu contains 35 items
# Use search tree to allocate 750 calories
# Total value of items taken = 719
#     9: <72, 182>
#     9: <85, 37>
#     14: <84, 144>
#     11: <57, 47>
#     10: <48, 57>
#     9: <61, 32>
#     7: <59, 70>
#     5: <56, 53>
#     4: <78, 95>
#     1: <29, 24>
#     0: <90, 5>
# Menu contains 40 items
# Use search tree to allocate 750 calories
# Total value of items taken = 725
#     9: <85, 37>
#     15: <53, 32>
#     14: <84, 144>
#     11: <57, 47>
#     9: <61, 32>
#     7: <59, 70>
#     15: <46, 31>
#     13: <5, 11>
#     12: <64, 154>
#     7: <15, 15>
#     5: <80, 60>
#     8: <47, 66>
#     3: <69, 46>
# Menu contains 45 items
# Use search tree to allocate 750 calories
# Total value of items taken = 811
#     4: <45, 65>
#     9: <85, 37>
#     6: <63, 3>
#     10: <48, 57>
#     9: <61, 32>
#     7: <59, 70>
#     15: <46, 31>
#     19: <80, 85>
#     17: <11, 21>
#     15: <81, 1>
#     14: <63, 75>
#     10: <17, 16>
#     6: <88, 95>
#     3: <64, 119>
# Menu contains 50 items
# Use search tree to allocate 750 calories
# Total value of items taken = 1148
#     4: <45, 65>
#     9: <85, 37>
#     6: <63, 3>
#     10: <48, 57>
#     9: <61, 32>
#     7: <59, 70>
#     15: <46, 31>
#     19: <80, 85>
#     17: <11, 21>
#     15: <81, 1>
#     14: <84, 106>
#     13: <85, 38>
#     11: <89, 20>
#     8: <89, 77>
#     5: <81, 7>
#     2: <75, 37>
#     1: <66, 20>
