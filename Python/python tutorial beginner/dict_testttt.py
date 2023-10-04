word = 'mentioned person: gender phone age'
new_word = word.split(' ')
dict = {'name':'oliver',
        'age':'29',
        'phone':'555-5555',
        'courses':['math','geography'],
        }
dict.update({'gender': 'male'})
del dict['name']
output = ''
for w in new_word:
    output += dict.get(w,w) + ' '
print(output)

print(dict.get('gender','notfound'))


print(new_word)