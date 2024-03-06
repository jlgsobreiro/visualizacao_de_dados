import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [1, 4, 9, 16, 25, 36]

plt.scatter(x, y, marker='P', color='r', s=100)
plt.plot(x, y, linestyle='dashdot', color='g', label='linha')
plt.title('Simple plot')
plt.xlabel('Time')
plt.ylabel('Distance')
plt.legend(['Distance', 'Dist'])
plt.grid(axis='y')
plt.show()
