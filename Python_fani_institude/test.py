def func(a):
    return a % 2 == 0
lst = [1,2,3,4,5,6]

lst2 = []
for i in lst:
    lst2.append(func(i))


a = list(filter(func,lst))
