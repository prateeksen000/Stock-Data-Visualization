import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,4,8,11,7]
eating = [3,4,6,2,9]
working = [7,8,2,2,6]
playing = [6,4,4,2,8]

plt.plot([],[],color='m',label='sleeping',linewidth=5)
plt.plot([],[],color='c',label='eating',linewidth=5)
plt.plot([],[],color='r',label='working',linewidth=5)
plt.plot([],[],color='k',label='playing',linewidth=5)

plt.stackplot(days, sleeping,eating,working,playing,colors=['m','c','r','k'])

plt.xlabel('x') 
plt.ylabel('y')
plt.title('Intersting graph\nChech it out')
plt.legend()
plt.show()
 
