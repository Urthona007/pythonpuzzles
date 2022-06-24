""" A grasshopper on a stick."""

### MATHY THOUGHTS ***
#from asyncio import constants


# n = num of middles
#
# TotalRange = 101 = R
# margin = 20 = M
# MiddleRange = R-(2*M)
# AreaMiddle = (R-(2*M))*n # rectange
# AreaEdge = M*(n/2)+M*(n/2)/2 # rectangle + mounted triange
# TotalArea = AreaMiddle + 2 * AreaEdge = 1000000 (hoping n is 11000)
#   (R-(2*M))*n + (M*(n/2)+M*(n/2)/2)*2 =
#   (R-(2*M))*n + Mn * Mn/2 =
#   Rn - 2Mn + Mn + Mn/2 =
#   n = TA / (R-2M+M+M/2) =
#   n = TA / (R-M/2)
#   Middle percentage n/TA = 1/(R-M/2)


# importing the required module
from random import random, randrange
import matplotlib.pyplot as plt

# x axis values
x = [*range(-50, 51)] # Note we are using centimeters, not meters!

# corresponding y axis values
y = [0]*101

NUM_TRIALS=1000000
TRIAL_LENGTH=100

for trial in range(NUM_TRIALS):
    pos = 0
    for tl in range(TRIAL_LENGTH):
        cat_range = 41
        cat_left_start = pos - 20
        if pos > 30:
            cat_range = 21+50-pos
            cat_left_start = pos - 20
        elif pos < -30:
            cat_range = 21+50+pos
            cat_left_start = -50
        pos = cat_left_start + randrange(cat_range)
        assert pos <= 50
        assert pos >= -50
    y[pos+50] += 1

# plotting the points
plt.plot(x, y)


# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Grasshopper location (cm)')

# function to show the plot
plt.show()
