###hashmaps are dictionaries in python

###1
# city_map = {}
# cities = ["calgary","vancouver","toronto"]
# cities2 = ["los angeles","new york","vegas"]

# city_map['canada'] = []
# city_map['canada'] += cities

# city_map['usa'] = []
# city_map['usa'] += cities2

# print(city_map)

 
###2
# cities = ["calgary","vancouver","toronto"]
# cities2 = ["los angeles","new york","vegas"]

# from collections import defaultdict
# city_map = defaultdict(list)

# city_map["Canada"] += cities
# city_map['usa'] += cities2

# print(city_map)


###anagram
### eg input:  strs = ["eat","tea","tan","ate","nat","bat"]
### output: [["bat"],["nat","tan"],["ate","tea","eat"]]

# from collections import defaultdict

# class Solution:
#     def GroupAnagrams(self,strs:list[str]) -> list[list[str]] :
#         anagram_map = defaultdict(list)
#         results = []

#         for s in strs:
#             sorted_s = tuple(sorted(s))                       
#             anagram_map[sorted_s].append(s)
#         # print(anagram_map)

#         for value in anagram_map.values():
#             results.append(value)

#         return results

# strs = ["eat","tea","tan","ate","nat","bat"]
# solution =  Solution()
# print(solution.GroupAnagrams(strs))  

###test

from collections import defaultdict

class Solution:
    def GroupAnagrams(self,strs:list[str]) -> list[list[str]] :
        anagram_map = defaultdict(list)
        results = []

        for s in strs:
            # sorted_s = tuple(sorted(s))                       
            anagram_map[(i for i in s)].append(s)
        # print(anagram_map)

        for value in anagram_map.values():
            results.append(value)

        return results

        # results.append(anagram_map.values())
        # print(results)

strs = ["eat","tea","tan","ate","nat","bat"]
solution =  Solution()
print(solution.GroupAnagrams(strs))  

