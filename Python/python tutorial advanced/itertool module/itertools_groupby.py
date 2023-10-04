import itertools
from operator import itemgetter

def get_state(person):
    return person['state']


people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

###if we ever need to change sorting
#### sorted_people = sorted(people,key=lambda person:person['city'])
#### for i in sorted_people:
####     print(i)


person_group = itertools.groupby(people,get_state)    ##get_state  ##itemgetter('state')  #lambda person:person['state']

###see the lists in that group
# for key,group in person_group:
#     print(key)
#     for i in group:
#         print(i)
#     print()


copy1, copy2 = itertools.tee(person_group)    ##make 2 copy of the list


##when we want to see eg how many in class got a or b or so on
for key, group in person_group:
    print(key, len(list(group)))
