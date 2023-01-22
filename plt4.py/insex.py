import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,3,6,7,5,4,3,9]

plt.scatter(x, y, label='skitscat', color='k',s=500, marker='8')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Intersting Graph\nCheck it out')
plt.legend()
plt.show()