import matplotlib.pyplot as plt
import numpy as np

# x = [1, 2, 3, 4, 5, 6]
y = [10, 25, 45]
labels = ['Water', 'Sand', 'Cement']
plt.pie(y,labels=labels, autopct='%1.1f%%', )
plt.title('Simple plot')
plt.xlabel('Time')
# plt.ylabel('Distance')
# plt.legend()
plt.show()
