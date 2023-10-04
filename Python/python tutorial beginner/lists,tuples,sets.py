list = ['ice cream','banana','forward','downward']
for x,y in enumerate(list,start=4):
    print(x,y)
list_str = ', '.join(list)
print((list_str))
new_list = list_str.split(',')
print((new_list))

