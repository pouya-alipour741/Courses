from collections import Counter

# Counting all items with count()

# To count the occurrences of items in l one can simply use a list comprehension and the count() method

l = ["a","b","b",'d','d']

# ###
# my_dict = dict()
# for i in l:
#     my_dict[i] = l.count(i)
# print(my_dict)
#
# #####
# my_dict2 = {i : l.count(i) for i in l}
# print(my_dict2)
# ###
# print([(x,l.count(x)) for x in set(l)])
#
# print(dict((x,l.count(x)) for x in set(l)))

# Alternatively, there's the faster Counter class from the collections library
l = ["a","b","b"]
print(Counter(l))
print(Counter(l).most_common(2))

