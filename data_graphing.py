# Arrays
import numpy as np

# Basic array functions
a1 = np.array([2,3,5])
a1.mean()
# 3.3333333333333335
a1.min()
# 2
a1.max()
# 5

# Array of 1's
np.ones(5)
# array([1., 1., 1., 1., 1.])

# Array of 0's
np.zeros(5)
# array([0., 0., 0., 0., 0.])

# Array of 5 elements from 0 to 1 (linearly spaced)
np.linspace(0,1,5)
# array([0.  , 0.25, 0.5 , 0.75, 1.  ])

# Array of 6 elements from 0 to 1 (linearly spaced)
np.linspace(0,1,6)
# array([0. , 0.2, 0.4, 0.6, 0.8, 1. ])

# Graph arrays
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,1,5)
y = np.array([1,2,3.5,10,20])
plt.plot(x,y,'ro')
plt.show()


# Scaling data to fit between 0 and 1.

# Number of kinds of teeth
# Wolf                33114423
# Brown Bat           23113333
# Rat                 22000066
# Human               22112233

Wolf = ['3', '3', '1', '1', '4', '4', '2', '3']
Rat = ['2', '2', '0', '0', '0', '0', '6', '6']

# Max is form the animal with the most of a tooth type.
scaleDict = {'identity': [1,1,1,1,1,1,1,1],
             '1/max': [1/3.0,1/4.0,1.0,1.0,1/4.0,1/4.0,1/6.0,1/6.0]}

# For each tooth, multiply the tooth by max, e.g.
for i in range(len(Wolf)):
    print float(Wolf[i]) *  scaleDict['1/max'][i]

# 1.0
# 0.75
# 1.0
# 1.0
# 1.0
# 1.0
# 0.333333333333
# 0.5

# For Rat this is...
# 0.666666666667
# 0.5
# 0.0
# 0.0
# 0.0
# 0.0
# 1.0
# 1.0


# Standard deviation:
# A measure that is used to quantify the amount of variation or dispersion of a set of data values.
# A low standard deviation indicates that the data points tend to be close to the mean (also called the expected value) of the set...
# while a high standard deviation indicates that the data points are spread out over a wider range of values.
# Reresented by the lower case Greek letter sigma σ for the population standard deviation or the Latin letter s for the sample standard deviation.
#
# For example a normal distribution (or bell-shaped curve) where each band has a width of 1 standard deviation.
#
# Gaussian distribution, another term for normal distribution.
# Uniform distribution, sometimes also known as a rectangular distribution, is a distribution that has constant probability.
# Exponential distribution, looks like an arc when graphed.
