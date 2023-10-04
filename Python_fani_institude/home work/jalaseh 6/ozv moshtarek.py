##a = [1,2,3,4,5]
##b = [4,5,6,7]
##c = []

#1
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
# print(c)

#2
a = [1,2,3,4,5]
b = [4,5,6,7]
c = []
for i in a:
    if i in b:
        c.append(i)

print(c)
