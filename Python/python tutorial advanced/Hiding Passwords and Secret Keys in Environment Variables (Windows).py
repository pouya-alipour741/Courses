import os

#gotta go to system setting and set environment variables
user1 = os.environ.get('my_user')  #work like dictionary
pass1 = os.environ.get('my_pass')

print(user1)
print(pass1)


