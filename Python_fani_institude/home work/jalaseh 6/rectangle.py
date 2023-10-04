#mostatil method 1

a = int(input('width: '))
b = int(input('length: '))
for i in range(a):
    output = ''
    for j in range(b):
        if i == 0 or i == (a-1) or j == 0 or j == (b-1):
            output += '*' + ' '
        else:
            output += ' ' + ' '
    print(output)


#method 2

# row = 5
# column = 20
# for i in range(row):
#     for j in range(column):
#         if i == 0 or i == 4 or j == 0 or j == 19:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print('')


#method 3
##a = int(input('width: '))
##b = int(input('length: '))
##        
##for i in range(a):
##    if i == 0:
##        print(b * '* ')
##    elif i > 0 and i < (a - 1):
##        print('* ', '  ' * (b-2),'*',sep= '')
##    elif i == (a-1):
##        print(b * "* ")
##    else:
##        print(' ')


#method 4
##a = int(input('width: '))
##b = int(input('length: '))
##
##output = ''
##for i in range(a):
##    if i == 0:
##        output += (b * '* ')
##    elif i > 0 and i < (a - 1):
##        output += '\n* '
##        output += '  ' * (b - 2)
##        output += '* '
##    elif i == (a - 1):
##        output += '\n' + b * "* "
##    else:
##        output += '  '
##print(output)

