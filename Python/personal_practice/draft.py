def find_index(to_search,target):
    for i,value in enumerate(to_search):
        if value == target:
            break
    else:
        return -1
    return i
    # else:                                 ####else in for/while loop means no break ,if break does not occur then it will always happen
    #     return -1
    # return i

my_lst = ['hhh','fff','ggg']

ind = find_index(my_lst,'ggg')
print(f'location of target index is: {ind}')

