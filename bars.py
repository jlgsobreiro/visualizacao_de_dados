import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [1, 4, 9, 16, 25, 36]
plt.bar(x, y)
plt.title('Simple plot')
plt.xlabel('Time')
plt.ylabel('Distance')
plt.legend(['Distance', 'Dist'])
plt.show()
