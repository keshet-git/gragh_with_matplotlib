import matplotlib.pyplot as plt
import numpy as np

# I'm using the lyrics of "Hey Jude" just for fun

labels = 'Na Na Na Na', 'Hey Jude', 'Other words'
sizes = [78, 15, 7]
# List of colors with the same length of the data
colors = ['b', 'g', 'r'] # Ugly colors but we want it fast

plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

plt.show()
