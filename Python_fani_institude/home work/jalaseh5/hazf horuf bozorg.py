# homework 2
# ref = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# s = input('word: ')
# i = 0
# sentence = ''
# while i < len(s):
#    if s[i] in ref:
#        sentence += s[i]
#    i += 1
# print(sentence)

#homework 2
output = ''
ref = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = input('word: ')
for i in s:
    if i not in ref:
        output = output + i
print(output)

