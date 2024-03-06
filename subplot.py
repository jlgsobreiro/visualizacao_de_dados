import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [1, 4, 9, 16, 25, 36]
z = [1, 5, 12, 13, 20, 30]
plt.subplot(2, 1, 1)
plt.title('Simple plot 1')
plt.xlabel('Time')
plt.ylabel('Distance')
plt.legend(['Distance', 'Dist'])
plt.plot(x, y)

plt.subplot(2, 1, 2)
plt.plot(x, z)
plt.title('Simple plot 2')
plt.xlabel('Time')
plt.ylabel('Distance')
plt.legend(['Distance', 'Dist'])
plt.show()
