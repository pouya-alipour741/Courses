import json

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

user = User("Max",29)
p = {"pouya":True}

# json.dumps(user)  ##will error so we write our own custom json encoder

##1
# def encode_user(o):
#     if isinstance(o, User):
#         return {"name": o.name, "age": o.age, o.__class__.__name__:True}
#     else:
#         raise TypeError("Object of type User is not JSON serializable")
#
# userJSON = json.dumps(user, default=encode_user)
# print(userJSON)


##2
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o: any) -> any:
        if isinstance(o, User):
            return {"name": o.name, "age":o.age, o.__class__.__name__:True}
        else:
            raise TypeError("Object of type User is not JSON serializable")


userJson = UserEncoder().encode(user)
print(userJson)


def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct


user = json.loads(userJson, object_hook=decode_user )
print(f"{user}, \ntype: {type(user)}, \nname: {user.name}")

