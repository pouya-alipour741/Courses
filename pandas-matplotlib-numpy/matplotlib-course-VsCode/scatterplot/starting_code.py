
import pandas as pd
from matplotlib import pyplot as plt
from contextlib import contextmanager
import os
from pathlib import Path

@contextmanager
def change_dir(directory):
    try:
        cwd = os.getcwd()
        os.chdir(directory)
        yield
    finally:
        os.chdir(cwd)


plt.style.use('seaborn')

x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]


colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
         538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

with change_dir(Path(__file__).parent):
    # print(Path(__file__).parent)
    data = pd.read_csv('2019-05-31-data.csv')


view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count,likes,c=ratio,cmap="summer",edgecolors="black", linewidth=1,alpha=0.5)

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()
