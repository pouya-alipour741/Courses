import requests
import json

url = r'https://api.giggl.app/v1/auth'

r = requests.get(url)
print(r.headers)
# print(r.content)
def loggin_site(username,password):
    s = requests.Session()  #this is for when we need cookies
    payload = {'email': username,'password': password}
    res = s.post(url, json=payload)
    # s.headers.update({'Authorization': json.loads(res.content)['token']})
    print(res.content)
    return s

session = loggin_site('pouya.alipour741@hotmail.com','Witch')




