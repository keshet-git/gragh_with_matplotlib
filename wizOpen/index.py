import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []

with open('uc.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter='.')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Loaded from file!')

#x, y = np.loadtxt('uc.txt', delimiter='.', unpack=True)

#plt.plot(x,y, label='Loaded from file!')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it ouy')
plt.legend()
plt.show()