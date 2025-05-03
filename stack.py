import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 6]
y2 = [1, 2, 4, 3, 5]

plt.stackplot(x, y1, y2, labels=['A', 'B'], alpha=0.75)
plt.legend(loc='upper left')
plt.show()