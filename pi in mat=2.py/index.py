import matplotlib.pyplot as plt
import numpy as np

# Same piece of code as 4.1
#--------------------------------------------
labels = 'Na Na Na Na', 'Hey Jude', 'Other words'
sizes = [78, 15, 7]

# This part is changed
#--------------------------------------------
colors = ['#e6ccff', '#b366ff', '#cc99ff'] # Sorry but I must change these ugly colors
# explode must be of legth sizes
explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hey Jude')

# add explode to plt.pie
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=90)

plt.axis('equal')
plt.show()