import matplotlib.pyplot as plt

#x = [1,2,3,4,5,6,7,8]
#y = [5,2,4,2,1,4,5,2]
days = [1,2,3,4,5]

plt.plot([],[], color ='m',label='Sleeping')
plt.plot([],[], color ='c',label='Eating')
plt.plot([],[], color ='r',label='Working')
plt.plot([],[], color ='k',label='Playing')



sleeping =[7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])
#scatter(x, y, label='skitscat', color='k', s=500, marker ='x')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it ouy')
plt.legend()
plt.show()