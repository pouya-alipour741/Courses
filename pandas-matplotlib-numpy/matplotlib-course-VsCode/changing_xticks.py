import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

x = [1,0,2,3,4,5]
y = [1,2,3,1,2,4]

plt.plot(x,y,c="black",marker="o",mfc="blue",ms=20)
plt.xticks(np.arange(0.5,7,0.5),[int(value) if np.floor(value)==value else value for value in np.arange(0.5,7,0.5)])
plt.yticks(np.arange(0.5,6,0.5))
file_dir = Path(__file__).parent
# plt.savefig(file_dir/"test2.png")
plt.show()

