import matplotlib.pyplot as plt
from pywaffle import Waffle


data = {'Water': 10, 'Sand': 25, 'Cement': 45}
plt.figure(
    FigureClass=Waffle,
    rows=5,
    values=data,
    legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)}
)
plt.title('Simple plot')
# plt.xlabel('Time')
# plt.ylabel('Distance')
# plt.legend(['Distance', 'Dist'])
plt.show()
