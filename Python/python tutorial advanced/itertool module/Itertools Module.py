import itertools
import operator

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3,2,1,0]
names = ['Corey', 'Nicole']


# counter = itertools.count(start=5,step=-2.5)       ##can use next() on it
#
# zip_data = zip(counter,numbers)
# print(list(zip_data))


# zip_data = zip(range(10),numbers)
# zip_data = itertools.zip_longest(range(10),numbers)
# print(list(zip_data))


counter= itertools.cycle([1,2,4])
# counter= itertools.cycle(('on','off'))
# counter = itertools.repeat(2)
# counter = itertools.repeat(2,times=3)   ###repeat only 3times

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


# counter = itertools.repeat(2)
#
# squares = map(pow,range(10),counter)
# squares = itertools.starmap(pow,[(2,2),(3,2),(5,2)])

# print(list(squares))

# result = itertools.combinations(letters,3)      ###tarkib 3tayi ,tartib mohem nist
# result = itertools.permutations(letters,3)      ###tarkib 3tayi ,tartib mohem hast
# result = itertools.product(numbers,repeat=4)      ####tarkib ba entekhab chand ozv va tartib mohem hast
# result = itertools.combinations_with_replacement(numbers,4)   # ####mesle bala
# result = itertools.islice(range(20),5)   ###slice until 5 numbers recalled
# result = itertools.islice(range(20),5,15,3)      ###start,end,steps
# for item in result:
#     print(item)

# combined = itertools.chain(letters,numbers,names)  ##instead of combined = letters + numbers + names which copies to a new list and takes so much memory in bigger lists
# for item in combined:
#     print(item)

##useful example for islice
# with open('test_sample.log','r') as f:
#     header = itertools.islice(f,3)
#
#     for line in header:
#         print(line,end='')


# selectors = [True,True,False,True]
# def lt_2(n):
#     return n < 2
#
#
# result = itertools.compress(letters,selectors)      ##compress similar to filter function but returns as iterator
# # result = filter(lt_2,numbers)
# # result = itertools.filterfalse(lt_2,numbers)      ##opposite of filter
# # result = itertools.dropwhile(lt_2,numbers)         #start at first true and goes to end of list
# # result = itertools.takewhile(lt_2,numbers)          ##stop at first false
# # result = itertools.accumulate(numbers)
# numbers2 = [1,2,3,4,5]
# # result = itertools.accumulate(numbers2,operator.mul)       ##mesle factorial  n!
# for item in result:
#     print(item)



