import json
import os
from urllib.request import urlopen

# # os.chdir(r'C:\Users\pouya\Desktop\python\Python Tutorial Supplementary Materials')

# #example 1 reading json into python then changing it and then saving it as json again
# with open(r'C:\Users\pouya\Desktop\python\Python Tutorial Supplementary Materials\states.txt', 'r') as f:
#     data = json.load(f)
#
# for state in data['states']:
#     del state["area_codes"]
#
#
#
# with open(r'C:\Users\pouya\Desktop\python\Python Tutorial Supplementary Materials\new_states.txt','w') as fi:
#     json.dump(data,fi,indent=2)


#example 2
user_inp = float(input('dollar amount: '))
with urlopen(r'http://www.floatrates.com/daily/usd.json') as response:
    source = response.read()
data = json.loads(source)

my_dict = dict()
for cur in data.items():
    name = cur[1]['name']
    rate = cur[1]['rate']
    my_dict[name] = rate

a = json.dumps(data,indent=2)
print(a)

print('dollar/euro = ',user_inp * float(my_dict['Euro']))


