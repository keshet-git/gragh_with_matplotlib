import matplotlib.pyplot as plt
import numpy as np

# Same piece of code as 4.2
#--------------------------------------------
sizes = [78, 15, 7]
colors = ['#e6ccff', '#b366ff', '#cc99ff'] 
explode = (0, 0.1, 0)

# This part is changed
#--------------------------------------------
labels = '78%  Na Na Na Na', '15%  Hey Jude', '7%   Other words'
patches, texts = plt.pie(sizes, colors=colors, explode=explode, startangle=90)
plt.legend(patches, labels, loc=(0.81,0)) # loc of x,y


plt.axis('equal')
plt.show()