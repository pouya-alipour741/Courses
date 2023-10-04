
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
# data = pd.read_csv(path)
# ages = data['Age']
# dev_salaries = data['All_Devs']
# py_salaries = data['Python']
# js_salaries = data['JavaScript']

# fig, ax = plt.subplots(nrows=2,ncols=2,sharex='row')  ##share x or y for when we have different lists,not practical in this example ##now it's a 2d array(2,2) #sharex='col','row','all',True

# ax[0,1].plot(ages, dev_salaries, color='#444444',
#          linestyle='--', label='All Devs')

# ax[1,0].plot(ages, py_salaries, label='Python')
# ax[1,1].plot(ages, js_salaries, label='JavaScript')

# ax[0,1].legend()
# ax[0,1].set_title('Median Salary (USD) by Age')
# ax[1,1].set_xlabel('Ages')
# ax[0,1].set_ylabel('Median Salary (USD)')

# ax[1,1].legend()
# ax[1,1].set_xlabel('Ages')
# ax[1,1].set_ylabel('Median Salary (USD)')

# ax[1,0].legend()
# ax[1,0].set_xlabel('Ages')
# ax[1,1].set_ylabel('Median Salary (USD)')

# fig.suptitle('super title')

# plt.tight_layout()

# plt.show()







#####2
data = pd.read_csv(path)
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig1, ax0 = plt.subplots()
fig2, ax1 = plt.subplots()

ax0.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax1.plot(ages, py_salaries, label='Python')
ax1.plot(ages, js_salaries, label='JavaScript')

ax0.legend()
ax0.set_title('Median Salary (USD) by Age')
ax0.set_ylabel('Median Salary (USD)')

ax1.legend()
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')

fig1.suptitle('super title 1')
fig2.suptitle('super title 2')

plt.tight_layout()

plt.show()

fig1.savefig('fig1.png')
fig2.savefig('fig2.png')
