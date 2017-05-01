import matplotlib.pyplot as plt
import numpy as np
#part 1 using csv
'''import csv

x = []
y = []
with open('Example.txt','r') as csvfile:
    plots = csv.reader(csvfile,delimiter = ',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y,label='Loaded from file')        
'''
#paart 2 using numpy ---- using numpy is easier
x,y = np.loadtxt('example.txt',delimiter=',',unpack=True)

plt.plot(x,y,label='Loaded from file')

plt.xlabel('x') 
plt.ylabel('y')
plt.title('Intersting pie chart\nCheck it out')
plt.legend()
plt.show()
 
