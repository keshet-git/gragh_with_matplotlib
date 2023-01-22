import matplotlib.pyplot as plt
import numpy as np

# Same piece of code as 4.3
#--------------------------------------------
sizes = [78, 15, 7]
colors = ['#e6ccff', '#b366ff', '#cc99ff'] 
explode = (0, 0.1, 0)
labels = '78%  Na Na Na Na', '15%  Hey Jude', '7%   Other words'
patches, texts = plt.pie(sizes, colors=colors, explode=explode, startangle=90)
plt.legend(patches, labels, loc=(0.81,0))

# This part is changed
#--------------------------------------------
plt.title("Breakdown of Lyrics to \"Hey Jude\"")


plt.axis('equal')
plt.show()