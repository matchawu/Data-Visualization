# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import random


fig = pyplot.figure()
ax = Axes3D(fig)

sequence_containing_x_vals = list(range(0, 100))
sequence_containing_y_vals = list(range(0, 100))
sequence_containing_z_vals = list(range(0, 100))

random.shuffle(sequence_containing_x_vals)
random.shuffle(sequence_containing_y_vals)
random.shuffle(sequence_containing_z_vals)

ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
pyplot.show()

#%%
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def make_dashedLines(x,y,z,ax):
    for i in range(0, len(x)):
        x_val, y_val, z_val = x[i],y[i],z[i]
        ax.plot([0,x_val],[y_val,y_val],zs=[0,0], linestyle="dashed",color="black")
        ax.plot([x_val,x_val],[0,y_val],zs=[0,0], linestyle="dashed",color="black")
        ax.plot([x_val,x_val],[y_val,y_val],zs=[0,z_val], linestyle="dashed",color="black")

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
x = [1,1,-1]
y = [1,-1,1]
z = [1,1,-1]

ax.scatter( x,y,z, c='r', marker='o')
make_dashedLines(x,y,z,ax)

# Make a 3D quiver plot
x, y, z = np.array([[-2,0,0],[0,-2,0],[0,0,-2]])
u, v, w = np.array([[4,0,0],[0,4,0],[0,0,4]])
ax.quiver(x,y,z,u,v,w,arrow_length_ratio=0.1, color="black")
ax.grid(False)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_zlim(-2,2)

plt.show()