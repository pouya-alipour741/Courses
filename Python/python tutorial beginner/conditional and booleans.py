user = 'admin'
logged_in = False
if user == 'admin' and  not logged_in:
    print('authorized')
else:
    print('not authorized')
if not logged_in:
    print('please log in')
else:
    print('welcome')