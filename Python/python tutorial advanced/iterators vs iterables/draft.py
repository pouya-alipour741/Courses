class Person():
    def __init__(self,first,famil):
        self.first = first
        self.last = famil

person = Person('ali','gholizadeh')


person_info = {'first':'pouya','last':'alipour'}

for key,value in person_info.items():
    setattr(person,key,value)

for key in person_info.keys():
    print(getattr(person,key))