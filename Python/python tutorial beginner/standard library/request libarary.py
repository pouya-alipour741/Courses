import requests

# r = requests.get(r'https://www.nexusmods.com/skyrimspecialedition/mods/5319')
# print(r.text)

###use dir(r) or help(r) to get more info of methods available to us

# i = requests.get(r'https://media.istockphoto.com/photos/orange-isolated-on-white-background-clipping-path-full-depth-of-field-picture-id1194662606?k=20&m=1194662606&s=612x612&w=0&h=Q3bHkLexn71hPlUJQSPhazlJiL-xpeVGwOAFwO67WcU=')

# with open('orange.png','wb') as f:
#     f.write(i.content)

# print(i.status_code) #print(r.ok)  status code :200 ok 300 redirection 400:client error 500: server error

# # print(i.headers)

payload = {'page': 2, 'count' : 25} #to auto generate url with these data
# h = requests.get(r'http://httpbin.org/get',params=payload)
# print(h.text)
# print(h.url)

p = requests.post(r'http://httpbin.org/post',params=payload)
print(p.text)
# print(p.content)

# payload = {'username': 'pouya', 'password' : 'test','something':'some'}
# payload2 = {'page':2,'count':45}
# p = requests.post('http://httpbin.org/post',data=payload,params=payload2)
# print(p.json())
# r_dict = p.json()
# print(r_dict.get('form'))


# r = requests.get('http://httpbin.org/basic-auth/pouya/test',auth=('pouya','test'))
# print(r.text)

# r = requests.get('http://httpbin.org/delay/4',timeout=3) #timeout should be used for most cases to prevent hangs
# print(r)



