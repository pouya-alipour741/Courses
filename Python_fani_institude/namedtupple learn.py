from collections import namedtuple

Car = namedtuple('Car_type',('cheverollete','mazda', 'bmw'))
Pouya = Car('have a blue one','dont have','have a silver one')
print(Pouya._asdict())
print(Pouya.mazda)
print(Pouya.cheverollete)
print(Pouya._fields)


