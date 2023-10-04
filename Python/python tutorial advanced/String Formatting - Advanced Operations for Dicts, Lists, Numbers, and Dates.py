import datetime
# for i in range(1,11):
#     sentence = 'the value is {:09}'.format(i)
#     print(sentence)

for i in range(10,20):
    sentence = f'the value is {i:04}'
    print(sentence)

# pi = 3.14159265
# sentence = f'the value is {pi:.3f}'
# print(sentence)

# sentence = f'1MB is equal to {1000**3:,.4f} bytes' # seperate each 3 digits with ,
# print(sentence)

my_date = datetime.datetime(2022,9,11,22,4,54)
sentence = f'{my_date:%Y %B,%d} fell on a {my_date:%A} and was the {my_date:%j} day of the year'
print(sentence)
print(my_date.strftime('%Y %B,%d'))   #just to remind both do the same
sentence = f"{my_date.strftime('%Y %B,%d')} fell on a {my_date.strftime('%A')} and was the {my_date.strftime('%j')} day of the year"
print(sentence)