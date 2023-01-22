import matplotlib.pyplot as plt

#x = [1,2,3,4,5,6,7,8]
#y = [5,2,4,2,1,4,5,2]
days = [1,2,3,4,5]


sleeping =[7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

slices = [7,2,2,13]
activities =['sleeping','eating','working','playing']
cols = ['c','m','r','b']
#scatter(x, y, label='skitscat', color='k', s=500, marker ='x')

plt.pie(slices, 
        labels=activities, 
        colors=cols, 
        startangle=90,
        shadow= True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it ouy')
plt.legend()
plt.show()