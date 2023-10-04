
# def find_index(to_search,target):
#     for i,value in enumerate(to_search):
#         if value == target:
#             break
#     else:                                 ####else in for/while loop means no break ,if break does not occur then it will always happen
#         return -1
#     return i
#
# my_lst = ['hhh','fff','ggg']
#
# ind = find_index(my_lst,'gg')
# print(f'location of target index is: {ind}')

###2
i = 0
while i < 50 :
    print(i)
    i += 1
    if i == 10:
        break
else:
    print('done')


