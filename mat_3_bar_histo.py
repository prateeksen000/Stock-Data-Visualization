import matplotlib.pyplot as plt
'''
x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,9,11]
y2 = [7,8,2,4,2]

plt.bar(x,y,label='bar1', color='r')
plt.bar(x2,y2,label='bar2', color='g')
'''
population_ages = [22,36,77,55,99,22,89,120,55,72,9,43,36,35,54,22,110,102]

#ids = [x for x in range(len(population_ages))]

bins = [0,10,20,30,40,50,60,70,80,90,110,120,130]

#plt.bar(ids,population_ages)

plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)

plt.xlabel('x') 
plt.ylabel('y')

plt.title('Intersting graph\nChech it out')
plt.show()
 
