
import pandas as pd
from matplotlib import pyplot as plt
from pathlib import Path
import os

plt.style.use('seaborn')

# cur_path = os.getcwd()
# path = os.path.join(cur_path,r'matplotlib-course\10-CoreySchafer\data.csv')

cur_dir = Path(__file__).parent
path = Path(cur_dir)/'data.csv'

####1
# a = 10

# def something():
    
#     a = 15
#     print('inside',a)
    
#     a = 20
#     a = 21
#     print('inside_local',a)

#     globals()['a'] = 150

# something()

# print('out',a)

import random

a = [1,2,3,4,5,6,7]
print(random.sample(range(len(a)),2))








#####2
# data = pd.read_csv(Path().glob('*/*.csv'))
# ages = data['Age']
# dev_salaries = data['All_Devs']
# py_salaries = data['Python']
# js_salaries = data['JavaScript']

# fig1, ax0 = plt.subplots()
# fig2, ax1 = plt.subplots()

# ax0.plot(ages, dev_salaries, color='#444444',
#          linestyle='--', label='All Devs')

# ax1.plot(ages, py_salaries, label='Python')
# ax1.plot(ages, js_salaries, label='JavaScript')

# ax0.legend()
# ax0.set_title('Median Salary (USD) by Age')
# ax0.set_ylabel('Median Salary (USD)')

# ax1.legend()
# ax1.set_xlabel('Ages')
# ax1.set_ylabel('Median Salary (USD)')

# fig1.suptitle('super title 1')
# fig2.suptitle('super title 2')

# plt.tight_layout()

# plt.show()

# fig1.savefig('fig1.png')
# fig2.savefig('fig2.png')

# print(Path().absolute())
print(list(Path().glob('*/*/*.csv')))