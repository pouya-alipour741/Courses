nums = [8,1,2,2,3]


###solution: we want to compare indexes so we use range(len())
output = []
# for i in range(len(nums)):
#     count = 0
#     for j in range(len(nums)):
#         if j != i and nums[j] < nums[i]:
#             count += 1

#     output.append(count)

# print(output)   



###testing
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         print(i,j)

###testing
# for i in range(1,10):
#     for j in range(1,10):
#         print(f"{i*j:>5}",end=" ")
#     print()


##draft
# nums = [8,1,2,2,3]
# out = []

# for i in range(len(nums)):
#     count = 0
#     for j in range(len(nums)):
#         if i != j and nums[i] > nums[j]:
#             count+=1
    
#     out.append(count)

# print(out)




