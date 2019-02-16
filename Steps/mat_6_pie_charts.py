import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,4,8,11,7]
eating = [3,4,6,2,9]
working = [7,8,2,2,6]
playing = [6,4,4,2,8]


slices = [7,9,6,8]
activities = ['sleping','eating','working','playing']

cols = ['c','m','r','b']
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.05,0,0),
        autopct='%1.1f%%')

#plt.xlabel('x') 
#plt.ylabel('y')
plt.title('Intersting pie chart\nCheck it out')
#plt.legend()
plt.show()
 
