class Person:
    def __init__(self,x):
        self.x = x

    def talk(self):
        print(f'hi, I am {self.x}')


person = Person('pouya')
print(person.x)

bob = Person('Bob')
bob.talk()