import matplotlib.pyplot as plt
import numpy as np

xpoints = []
for point in range(-10,10):
    xpoints.append(point)
    


ypoints = []
for point in xpoints:
    ypoints.append(point * point + 2)
plt.plot(xpoints, ypoints, color = 'r')

y2points = []
for point in xpoints:
    y2points.append(point * point * point + 3)

plt.plot(xpoints, y2points, color = 'b')

plt.show()