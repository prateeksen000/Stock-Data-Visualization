from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = fig.add_subplot(111, projection='3d')

x = [1,2,3,4,5,6,7,8,9,10]
y = [3,6,6,7,7,4,4,6,8,3]
z = [1,4,4,2,6,7,4,5,8,3]

#ax1.plot_wireframe(x,y,z)

x2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y2 = [-3,-6,-6,-7,-7,-4,-4,-6,-8,-3]
z2 = [1,4,4,2,6,7,4,5,8,3]

ax1.scatter(x,y,z,c='g',marker='o')
ax1.scatter(x2,y2,z2,c='r',marker='o')

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()
