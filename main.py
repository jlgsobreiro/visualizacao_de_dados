import matplotlib.pyplot as plt
import numpy as np

# x = [1, 2, 3, 4, 5, 6]
# y = [1, 4, 9, 16, 25, 36]
# z = [1, 5, 12, 13, 20, 30]

x = np.arange(-10, 10, 0.01)
y = np.sin(x)
z = np.cos(x)
plt.plot(x, z)
plt.plot(x, y)
plt.title('Simple plot')
plt.xlabel('Time')
plt.ylabel('Distance')
plt.legend(['Distance', 'Dist'])
plt.show()
