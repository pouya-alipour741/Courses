nums = [1,2,3,4,5,6,7,8,9,10]

# my_list = [] #ex1
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

#example above turned into list_comprehension
# my_list = [n*n for n in nums]
# print(my_list)

#using map+lambda  #99% of the time you can use list comprehension instead of lambda for much better readablity and you should do that instead ,just example:
# my_list = list(map(lambda n: n*n, nums))
# print(my_list)


# my_list = [] #ex2
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)
#
# my_list = [n for n in nums if n%2==0]
# print(my_list)

# my_list = list(filter(lambda n:n%2==0,nums))
# print(my_list)


# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num))
# print(my_list)
#
# my_list = [(letter,num) for letter in 'abcd'for num in range(4)]
# print(my_list)


# names = ['Bruce','Clark','Logan','Peter','Wade']
# heros = ['Wayne','Superman','Spiderman','Wolverine','Deadpool']
# my_dict = {}
# for name,hero in zip(names,heros):
#     my_dict[name] = hero
# print(my_dict)

# my_dict = {name: hero for name, hero in zip(names, heros) if name!= 'Peter'}
# print(my_dict)


# nums = [1,1,1,2,3,2,2,2,4,5,6,7,5,5,8,9,10,4,8,7]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

# my_set = {n for n in nums}
# print(my_set)


# def gen_func(nums):
#     for n in nums:
#         yield n*n
#
# my_gen = gen_func(nums)
#
# for i in my_gen:
#     print(i)

# my_gen = (n*n for n in nums)
# for i in my_gen:
#     print(i)


###more examples

# fruits = ['apple','orange','bananas']
#
# new_fruits = []
#
# for fruit in fruits:
#     fruit = fruit.upper()
#     new_fruits.append(fruit)
#
# fruits = new_fruits
# print(fruits)

# new_fruits = [fruit.upper() for fruit in fruits]
#
# print(new_fruits)

####
# bits = [False,True,False,False,True,False]
#
# new_bits = [1 if bit == True
#             else  0
#             for bit in bits]
# print(new_bits)

#####
# my_string = 'HelloMyNameIsPouya'
# new_str = []
# for i in my_string:
#     if i.isupper():
#         i = ' ' + i
#     new_str.append(i)
#
# my_string = ''.join(new_str)
# print(my_string[1:])

# new_string = ''.join([' ' + i if i.isupper()
#                     else ' ' + i.lower() if i in ['N','I']
#                     else i
#                     for i in my_string])[1:]
# print(new_string)


####
# my_dict = {
#             'name':'mario',
#             'profession':'plumber'
# }
# print(my_dict.items())

# my_dict = {key:'super ' + val for key,val in my_dict.items()}
# print(my_dict)

####another example
# names = ['fdsf1','FHFDSJ4','fgvfbhc3']
# new_names = []
#
# for n in names:
#     if n.islower():
#         n = n.capitalize()
#     else:
#         n = "Relax " + n.capitalize()
#
#     new_names.append(n)
#
# print(new_names)


# names = ['fdsf1','FHFDSJ4','fgvfbhc3']
# new_names = [n.capitalize() if n.islower()
#              else 'Relax ' + n.capitalize()
#                 for n in names]
#
# print(new_names)



####another example
# my_str = 'hi442nm233ag2'
#
# new_str = ''.join([
#     'd' if i == '4'
#     else 'e' if i == '2'
#     else 's' if i == '3'
#     else i
#     for i in my_str
# ])
#
# print(new_str)


