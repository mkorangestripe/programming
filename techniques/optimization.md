# Optimization, the 0/1 Knapsack problem

```python
class Food:
    def __init__(self, name, value, calories):
        self.name = name
        self.value = value
        self.calories = calories
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'
```

### Greedy Algorithm

A brute force algorithm for generating all combinations can take too long.  
A greedy algorithm doesn't always yield the best solution and doesn't show how close the approximation is.  
Here's a greedy algorithm using calories as a limiting factor.  
The results are computed by value, calories, or the ratio of value/calories.  
In this example 'greedy by value' produced the highest total value <= the calorie limit.

```python
def buildMenu(names, values, calories):
    """
    names, values, calories: lists of same length
    name: list of strings
    values calories: lists of numbers
    return a list of Foods
    """

    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu

def greedy(items, maxCost, keyFunction):
    """
    Assume 'items' is a list, maxCost >= 0,
    keyFunction maps elements of items to numbers
    """

    itemsCopy = sorted(items, key=keyFunction, reverse=True)
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
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)

    print('\nUse greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))

    print('\nUse greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)
```

```python
names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]

foods = buildMenu(names, values, calories)
testGreedys(foods, 1000)
```

```
Use greedy by value to allocate 1000 calories
Total value of items taken = 424.0
    burger: <100, 354>
    pizza: <95, 258>
    beer: <90, 154>
    wine: <89, 123>
    apple: <50, 95>

Use greedy by cost to allocate 1000 calories
Total value of items taken = 413.0
    apple: <50, 95>
    wine: <89, 123>
    cola: <79, 150>
    beer: <90, 154>
    donut: <10, 195>
    pizza: <95, 258>

Use greedy by density to allocate 1000 calories
Total value of items taken = 413.0
    wine: <89, 123>
    beer: <90, 154>
    cola: <79, 150>
    apple: <50, 95>
    pizza: <95, 258>
    donut: <10, 195>
```

### Memoization

This is an example of the 0/1 knapsack problem using memoization to reduce redundancy.

```python
import random

def buildLargeMenu(numItems, maxVal, maxCost):
    """
    Return a list of food items as objects with a random value and caloric cost
    """

    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items

def fastMaxVal(toConsider, avail, memo={}):
    """
    Assume toConsider is a list of subjects, avail is a weight.
    memo is supplied by recursive calls.
    Return a tuple of the total value of the solution to the
    0/1 knapsack problem and the subjects of that solution.
    """

    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:  # check whether food item list is empty or remaining calories is 0
        result = (0, ())
    elif toConsider[0].getCost() > avail:  # check whether food item[0] calories > remaining calories
        # Explore right branch only:
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]

        # Explore left branch:
        withVal, withToTake = fastMaxVal(toConsider[1:], avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()

        # Explore right branch:
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail, memo)

        # Choose better branch:
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)

    memo[(len(toConsider), avail)] = result

    return result
```

Example of fastMaxVal():

```
items:
item, value, calories
0: <20, 9>
1: <73, 62>
2: <81, 182>
3: <81, 43>
4: <31, 199>
5: <17, 14>
6: <85, 139>
7: <67, 115>
8: <64, 145>
9: <45, 137>

Start down the left branch...
fastMaxVal(items, 750)
nextItem = '0: <20, 9>'
withVal, withToTake = fastMaxVal(items[1:], 741, memo)
nextItem = '1: <73, 62>'
withVal, withToTake = fastMaxVal(items[1:], 679, memo)
nextItem = '2: <81, 182>'
withVal, withToTake = fastMaxVal(items[1:], 497, memo)
nextItem = '4: <31, 199>'
withVal, withToTake = fastMaxVal(items[1:], 454, memo)
nextItem = '5: <17, 14>'
withVal, withToTake = fastMaxVal(items[1:], 255, memo)
nextItem = '6: <85, 139>'
withVal, withToTake = fastMaxVal(items[1:], 241, memo)
nextItem = '7: <67, 115>'
withVal, withToTake = fastMaxVal(items[1:], 102, memo)
toConsider[0].getCost() > avail: # 115 > 102
result = fastMaxVal(toConsider[1:], avail, memo) -- This is 'items 8 and 9', 102, memo
Repeat with only item 8, then only item 9
toConsider == []
result = (0, ())
Step back a few lines...
withVal, withToTake = 0, ()
Proceed with next steps...
withVal += nextItem.getValue() -- This is 0 += 64 = 64
Now do the same as above with remaing two items, 8 and 9
This is considered the right branch now
withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
                                       avail, memo)
Then it looks like these two branches are compared for value.
And the memoization starts to happen.
```

```python
def testMaxVal(foods, maxUnits, algorithm, printItems=True):
    print('Menu contains', len(foods), 'items')
    print('Use search tree to allocate', maxUnits, 'calories')

    val, taken = algorithm(foods, maxUnits)

    if printItems:
        print('Total value of items taken =', val)
        for item in taken:
            print('   ', item)

# For each number of food items(numItems), create an items list with random value and caloric cost.
# Then determine the combination of food with the largest value less than the maximum calories.

for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, fastMaxVal, True)
```

```
Use search tree to allocate 750 calories
Total value of items taken = 299
    4: <59, 51>
    3: <89, 82>
    2: <12, 67>
    1: <53, 122>
    0: <86, 192>
Menu contains 10 items
Use search tree to allocate 750 calories
Total value of items taken = 410
    9: <69, 71>
    7: <70, 175>
    6: <26, 8>
    5: <70, 116>
    3: <90, 242>
    1: <55, 4>
    0: <30, 94>
Menu contains 15 items
Use search tree to allocate 750 calories
Total value of items taken = 648
    14: <85, 22>
    13: <87, 115>
    11: <69, 231>
    9: <71, 34>
    8: <76, 15>
    7: <81, 8>
    6: <1, 28>
    5: <54, 44>
    4: <55, 83>
    0: <69, 166>
Menu contains 20 items
Use search tree to allocate 750 calories
Total value of items taken = 716
    14: <85, 22>
    13: <87, 115>
    9: <71, 34>
    8: <76, 15>
    7: <81, 8>
    10: <64, 150>
    8: <37, 12>
    6: <47, 1>
    5: <24, 39>
    4: <63, 123>
    2: <81, 215>
Menu contains 25 items
Use search tree to allocate 750 calories
Total value of items taken = 857
    14: <85, 22>
    13: <87, 115>
    9: <71, 34>
    8: <76, 15>
    7: <81, 8>
    5: <54, 44>
    4: <55, 83>
    8: <37, 12>
    6: <47, 1>
    5: <24, 39>
    8: <78, 37>
    7: <70, 49>
    3: <32, 111>
    2: <53, 124>
    1: <7, 1>
Menu contains 30 items
Use search tree to allocate 750 calories
Total value of items taken = 997
    14: <85, 22>
    13: <87, 115>
    9: <71, 34>
    8: <76, 15>
    7: <81, 8>
    5: <54, 44>
    4: <55, 83>
    8: <37, 12>
    6: <47, 1>
    5: <24, 39>
    8: <78, 37>
    7: <70, 49>
    10: <90, 82>
    8: <10, 122>
    1: <80, 24>
    0: <52, 8>
Menu contains 35 items
Use search tree to allocate 750 calories
Total value of items taken = 1017
    14: <85, 22>
    13: <87, 115>
    9: <71, 34>
    8: <76, 15>
    7: <81, 8>
    5: <54, 44>
    4: <55, 83>
    8: <37, 12>
    12: <30, 11>
    11: <41, 104>
    19: <84, 17>
    15: <86, 55>
    13: <32, 43>
    11: <74, 15>
    9: <20, 22>
    7: <42, 57>
    3: <62, 38>
Menu contains 40 items
Use search tree to allocate 750 calories
Total value of items taken = 1033
    14: <85, 22>
    13: <87, 115>
    9: <71, 34>
    8: <76, 15>
    7: <81, 8>
    13: <78, 78>
    12: <30, 11>
    8: <78, 37>
    10: <90, 82>
    11: <74, 15>
    15: <68, 95>
    10: <81, 83>
    3: <55, 91>
    1: <79, 60>
Menu contains 45 items
Use search tree to allocate 750 calories
Total value of items taken = 1270
    14: <85, 22>
    9: <71, 34>
    8: <76, 15>
    12: <87, 54>
    8: <37, 12>
    6: <47, 1>
    8: <78, 37>
    7: <70, 49>
    10: <90, 82>
    11: <74, 15>
    17: <81, 81>
    15: <21, 36>
    14: <41, 3>
    12: <81, 69>
    9: <82, 31>
    7: <89, 88>
    5: <86, 91>
    4: <74, 7>
Menu contains 50 items
Use search tree to allocate 750 calories
Total value of items taken = 1270
    14: <85, 22>
    9: <71, 34>
    8: <76, 15>
    12: <87, 54>
    8: <37, 12>
    6: <47, 1>
    8: <78, 37>
    7: <70, 49>
    10: <90, 82>
    11: <74, 15>
    17: <81, 81>
    15: <21, 36>
    14: <41, 3>
    12: <81, 69>
    9: <82, 31>
    7: <89, 88>
    5: <86, 91>
    4: <74, 7>
```
