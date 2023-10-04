from typing import List
from collections import defaultdict,Counter

###1  doesn't work correctly
# class Solution:
#     def destCity(self,paths:List[List[str]]) -> str:
#         outgoing_count = defaultdict(int)
#         for path in paths:
#             city_a, city_b = path
#             outgoing_count[city_a] += 1
#             outgoing_count[city_b] += 1
#         # print(outgoing_count)
#         for city in outgoing_count:
#             print(city)


# paths = [["London","New York"],["New York", "Lima"],["Lima","Sao Paulo"]]
# paths2 = [["b","c"],["c", "a"],["d","b"]]

# solution = Solution()
# solution.destCity(paths)



###2  
# class Solution:
#     def destCity(self,paths:List[List[str]]) -> str:
#         outgoing_count = {}
#         for path in paths:
#           city_a, city_b = path
#           ###if it's not in start point then it's out final destination
#           outgoing_count[city_a] = outgoing_count.get(city_a, 0) + 1
#           outgoing_count[city_b] = outgoing_count.get(city_b, 0) 
#         print(outgoing_count) #debug
#         print(outgoing_count.get("London",0)) #debug

#         for city in outgoing_count:
#            if outgoing_count[city] == 0:
#               return city


# paths = [["London","New York"],["New York", "Lima"],["Lima","Sao Paulo"],["New York","London"]]
# paths2 = [["b","c"],["c", "a"],["d","b"]]

# solution = Solution()
# print(solution.destCity(paths))



##3
# class Solution:
#     def destCity(self,paths:List[List[str]]) -> str:
#         a, b = map(set ,zip(*paths))
#         # print(f"{a}\n{b}\n{b-a}") #debug
#         return (b-a).pop()

# paths = [["New York", "Lima"],["Lima","Sao Paulo"],["London","New York"]]
# paths2 = [["b","c"],["c", "a"],["d","b"]]


# solution = Solution()
# print(solution.destCity(paths))


# #testing
# # a, b = map(set ,zip(*paths))
# # print((b-a).pop())


# a, b = map(set, zip(*paths))   ##testing
# print(b.difference(a))  ##we can get the item with .pop() same as above
