#homework 4 while
# sentence = input('> ')
#
# i = 1
# output = ''
# while i < len(sentence):
#     output = output + sentence[i]
#     i = i + 2
# print(output)


#homework 4 for
# sentence = input('> ')
# output = ''
# for i in range(1,len(sentence),2):
#     output += sentence[i]
#
# print(output)


#homework 4 while

# s = input('> ')
# i = 0
# output = ''
# while i < len(s):
#     if i % 2 != 0:
#         i = i + 1
#         continue
#     else:
#         output = output + s[i]
#         i = i + 1
# print(output)
#
# #homework 4 for
# s = input('> ')
# output = ''
# for i in range(0,len(s)):
#     if i % 2 != 0:
#         continue
#     else:
#         output = output + s[i]
# print(output)

#generator
# s = ''.join(sentence[i] for i in range(0,len(sentence),2))
# print(s

#generator 2
s = ''.join([j for i,j in enumerate(sentence) if i % 2 == 0])
print(s)



