import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

x2 =[1,2,3]
y2 =[10,15,11]

plt.plot(x,y, label='First line')
plt.plot(x2,y2, label='Second lineS')
plt.xlabel('plot Numer')
plt.ylabel('Improteant var')

plt.title('Interesing Graph\nCheck it out')
plt.legend()
plt.show()