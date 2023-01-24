import matplotlib.pyplot as plt

a = [0, -100, 25, 67, -323]
b = [0,3,7,3,9]
plt.axis([-50, 80,2,8])
plt.xticks((-40,-20,0,20,40,60,80),('k','e','s','h','e','t','A'))
plt.title('Triangle')
plt.xlabel('Array A')
plt.ylabel('Array B')
plt.plot(a,b, color='red')
plt.show()