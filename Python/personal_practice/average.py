from statistics import mean

####mean method
# inp_lst = [12, 45, 78, 36, 45, 237.11, -1, 88]
# list_avg = mean(inp_lst)
#
# print("Average value of the list:\n")
# print(list_avg)
# print("Average value of the list with precision upto 3 decimal value:\n")
# print(round(list_avg,3))

###sum and len method
# inp_lst = [12, 45, 78, 36, 45, 237.11, -1, 88]
#
# sum_lst = sum(inp_lst)
#
# lst_avg = sum_lst/len(inp_lst)
# print("Average value of the list:\n")
# print(lst_avg)
# print("Average value of the list with precision upto 3 decimal value:\n")
# print(round(lst_avg,3))


###reduce method and for loop method
# from functools import reduce
#
# inp_lst = [12, 45, 78, 36, 45, 237.11, -1, 88]
#
# lst_len= len(inp_lst)
#
# lst_avg = reduce(lambda x, y: x + y, inp_lst) /lst_len
# print("Average value of the list:\n")
# print(lst_avg)
# print("Average value of the list with precision upto 3 decimal value:\n")
# print(round(lst_avg,3))
#
# product = 0
# for i in inp_lst:
#     product += i
# print('\nfor loop method of reduce function :')
# print(product/len(inp_lst))
# print('round up: ',round(product/len(inp_lst)))



#operator method instead of lambda
# from functools import reduce
# import operator
# inp_lst = [12, 45, 78, 36, 45, 237.11, -1, 88]
#
# lst_len = len(inp_lst)
#
# lst_avg = reduce(operator.add, inp_lst) /lst_len
# print("Average value of the list:\n")
# print(lst_avg)
# print("Average value of the list with precision upto 3 decimal value:\n")
# print(round(lst_avg,3))

#numpy average

import numpy

inp_lst = [12, 45, 78, 36, 45, 237.11, -1, 88]

lst_avg = numpy.average(inp_lst)
print("Average value of the list:\n")
print(lst_avg)
print("Average value of the list with precision upto 3 decimal value:\n")
print(round(lst_avg,3))