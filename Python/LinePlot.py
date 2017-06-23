#!/usr/bin/python
# Corey Mutnik - 170622
# Let's start with a simple line plot

# import packages
import matplotlib.pyplot as plt

# define variables
x,y = [2,4,8], [2,4,8]

###
# Plot
###
plt.clf() # clear plot window

# set limits
plt.xlim(0,10)
plt.ylim(0,10)

# labels
plt.xlabel("X")
plt.ylabel("Y")
plt.title("First Plot")

plt.plot(x,y,"ok-") # plot data: 
                        # x vs y
                        # "k" designates the color as black
                        # "o" plots the points
                        # "-" connects the points with lines

# save figure
plt.savefig("lp.png")