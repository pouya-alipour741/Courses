word = 'mentioned person: gender phone age'
new_word = word.split(' ')
dict = {'name':'oliver',
        'age':'29',
        'phone':'555-5555',
        'courses':['math','geography']}
dict.update({'gender': 'male'})
del dict['name']

output = ''
for i in new_word:
    # print(i)
    output += dict.get(i,i) + ' '
    # print(dict.get(i,i))

print(output)

# for x,y in dict.items():
#     print(x,y)