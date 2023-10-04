# s1 = {1, 2, 3, 4, 5}
# s2 = {7, 8, 9}

# s1.add(50)
# print(s1)

# s1.update([6,7,8],s2)      ###could also use {6,7,8} to update s1
# print(s1)

# s1.remove(50)
# print(s1)

# s1.discard(9)     ###same as remove but if we try to discard a number that does not exist in set it does not give errors
# print(s1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3,4,5}

# s4 = s1.intersection(s2,s3)
# print(s4)
# s4 = s1.difference(s2)   ##values in s1 but not in s2
# print(s4)

# s4 = s1.difference(s2,s3)    ##values in s1 but not in s2 or s3
# print(s4)

# s4 = s2.difference(s1,s3)
# print(s4)

# s4 = s1.symmetric_difference(s3)       ####all the difference between s1 and s2
# print(s4)

##remove duplicates
# l1 = [1,2,3,1,2,3]
# l2 = list(set(l1))
# print(l2)


employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

gym_and_dev = set(gym_members).intersection(developers)
print(gym_and_dev)

result = set(employees).difference(gym_members,developers)
print(result)



# if 'Corey' in developers:
#     print('Found!')

# O(n) for list     ##working with sets is generally faster than lists
# O(1) for a set

