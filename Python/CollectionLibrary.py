from collections import defaultdict,OrderedDict,Counter,namedtuple,deque


###
# defaulted = defaultdict(list)

# for char in "cheese":
#     defaulted[char].append(char)

# print(defaulted)

###
# defaulted = defaultdict(int)

# for char in "cheese":
#     defaulted[char] += 1

# print(defaulted)

###
# defaulted = defaultdict(str)

# for char in "cheese":
#     defaulted[char] += "1"

# print(defaulted)

###
# defaulted = defaultdict(list)

# lst = ["torento","quebec","otava","otnerot"]

# for char in lst:
#     defaulted[tuple(sorted(char))].append(char)

# print(defaulted)


###
# defaulted = defaultdict(list)

# for char in "cheese":
#     defaulted[char].append(char)

# print(defaulted)

# # print(sorted(defaulted))

# ord_dic = OrderedDict(defaulted)
# ord_dic.move_to_end("c")
# print(ord_dic)
# print(ord_dic.popitem())  ##get last item
# print(ord_dic.popitem(False))   ##get first item


####
# d = deque("abcde")

# print(d)
# d.rotate(2)
# print(d)


# d = deque("abcde")
# print(d.popleft())


d = deque("abcde")
d.append("h")

print(d)

d.rotate(1)
print(d)