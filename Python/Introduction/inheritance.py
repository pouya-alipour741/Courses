class Mamal:
    def __init__(self,x):
        self.x = x
    def walk(self):
        print('walk')

class Dog(Mamal):
    def bark(self):
        print(f'most of dogs are {self.x}')

class Cat(Mamal):
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y
    def expres(self):
        print(f'most cats are {self.x} and all of them are {self.y}')

dog = Dog('loud')
print(dog.x)
#dog.bark()
#dog.walk()

cat = Cat('funny', 'cute')
print(cat.x)
print(cat.y)
cat.expres()





