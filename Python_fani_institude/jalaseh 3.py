#max of 3
##a=int(input('enter number 1: '))
##b=int(input('enter number 2: '))
##
##if a>b :
##    print('Number a bozorg tar ast',a)
##
##else:
##    print('Number b bozorg tar ast',b)




# User Pass Admin ?
user=input('enter Username: ')
password=input('enter Password: ')

user = user.lower().strip()
##user = user.strip()
password = password.lower()
password = password.strip()


if user == 'admin' and password == 'admin':
    print('you are administrator')

else :
    print('you are not administrator')


#1
##sentence =input('enter 3 char: ')
##new_sent = sentence[:3]
##
##ref = 'aeiuo'
##
##if new_sent[0] in ref or new_sent[1] in ref or new_sent[2] in ref:
##    print('vowel')
##else:
##    print('no vowel')



# sentence =input('enter 3 char: ')
#
# ref = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# if sentence[0] in ref or sentence[1] in ref or sentence[2] in ref:
#    print('there is capital letter')
# else:
#    print('there is no capital letter')

##sentence =input('enter 3 char: ')
##new_sentence = sentence[:10]
##ref = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
##
##for i in range(10):
##    if new_sentence[i] in ref:
##        print(new_sentence[i])







    


