class Duck:
    def quack(self):
        print('quack')
    def fly(self):
        print('fly')
class Person:
    def quack(self):
        print('imitate quack')
    def fly(self):
        print('imitate fly')

# def quack_fly(thing):
#     if isinstance(thing,Duck):  #non-pythonic
#         thing.quack()
#         thing.fly()
#     else:
#         print('not duck')

# def quack_fly(thing): #non-pytonic
#     if hasattr(thing,'quack'):
#         if callable(thing.quack):
#             thing.quack()
#
#     if hasattr(thing,'fly'):
#         if callable(thing.fly):
#             thing.fly()
#     print()  #print a blank line


# def quack_fly(thing): #pytonic
#     try:
#         thing.quack()
#         thing.fly()
#         thing.bark()
#     except AttributeError as e:
#         print(e)
#     print() #print a blank line


d = Duck()
quack_fly(d)
p = Person()
quack_fly(p)


