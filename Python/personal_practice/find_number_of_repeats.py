# def num_of_repeats(my_string):
#     first_index = 0
#     count = 0
#     for i in range(len(my_string)):
#         k = my_string.find('test',first_index)
#         if k != -1:
#             first_index = k+1
#             count += 1
#     return count

my_string5 = "test string test, test string testing, test string test string"
# print(num_of_repeats(my_string5))

##with while
first_index = 0
i = 0
count = 0
while i < len(my_string5) :
    k = my_string5.find('test', first_index)
    if k != -1:
        first_index = k+1
        count += 1
    i += 1
print(count)






