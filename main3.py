import matplotlib.pyplot as plt
import numpy as np

ca0 = 0.1
k = 1.3
cb0 = 0

dCa_dt = lambda n: -k * ca0 ** n
dCb_dt = lambda n: k * ca0 ** n

xat = lambda n, cx: (ca0 - cx(n)) / ca0

x = np.arange(0, 2, 0.01)
y = [xat(x, dCa_dt) for x in x]
z = [xat(x, dCb_dt) for x in x]

plt.plot(x, z)
plt.plot(x, y)
plt.title('Simple plot')
plt.xlabel('Time')
plt.ylabel('Distance')
plt.legend(['Distance', 'Dist'])
plt.show()
