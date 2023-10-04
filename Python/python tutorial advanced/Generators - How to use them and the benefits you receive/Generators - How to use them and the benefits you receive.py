# #normal function
# def square_func(nums):
#     results = []
#     for i in nums:
#         results.append(i*i)
#     return results

# print(square_func([1,3,5,4]))


# # turned into generator function ,we can save so much memory this way
# def square_func(nums):
#     for i in nums:
#         yield (i*i)
#
# my_nums = square_func([1,3,5,4])
# print(my_nums)
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))


#generator just like list comprehension but save memory and use() instead of []
# nums = [1,3,5,4]
# my_numbs = (i*i for i in nums)
# print(my_numbs)
# for n in my_numbs:
#     print(n)



