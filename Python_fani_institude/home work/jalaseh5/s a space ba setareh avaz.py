# s_1 = input('> ')
# s_2 = ''
#
# for letter in s_1:
#    if letter == ' ':
#        s_2 += '*'
#    elif letter == 's':
#        s_2 += '*'
#    elif letter == 'a':
#        s_2 += '*'
#    else:
#        s_2 = s_2 + letter
# print(s_2)


#method2
# blklist = 'sa '
# s = input('> ')
#
# for i in blklist:
#     s = s.replace(i,'*')
# print('method2: \n' +s+ '\n')
# #method3
# output = ''
# for i in s:
#     if i in blklist:
#         output += '*'
#     else:
#         output += i
# print('method3: \n', output, '\n')
#method4
blklist = 'sa '
s = input('> ')
output = ''
for i in s:
    output += ('*' if i in blklist else i)
print('method4: \n', output, '\n')

