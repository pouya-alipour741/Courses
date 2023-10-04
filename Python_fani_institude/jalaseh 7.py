#jadval zarb
##for i in range(1,11):
##    for j in range(1,11):
##        print('{:>5}'.format(i * j),end='')
##    print('')



## 3daneshjoo - code nam nomreh gerefte- dar ghaleb dictionary chap
# my_dict = {}
# for i in range(3):
#     code = input('code: ')
#     name = input('nam: ')
#     mark = input('nomreh: ')
#     my_dict[code] = [name, mark]   #or my_dict.update({code:[name,mark]})
#
# print(my_dict)


##w = int(input('arz: '))
##l = int(input('tool: '))
##def a_c_rectangle(w,l):
##    s = w * l
##    c = 2 * (w + l)
##    return "area = {}".format(s),"circum = {}".format(c)
##    
##print(a_c_rectangle(w,l))



#ekhtelaf masahat mostatil dayereh - kodam bozorgtar
##w = int(input('arz: '))
##l = int(input('tool: '))
##r = int(input('shoa: '))


##def mostatil(w,l):
##    r = w * l
##    return r
##
##def dayereh(r):
##    c = 3.14 * r ** 2
##    return c
##
##def ekhtelaf():
##    if mostatil(w,l) > dayereh(r):
##        print('mostatil > dayereh -','ekhtelaf masahat = ',mostatil(w,l) - dayereh(r))
##    else:
##        print('dayereh > mostatil -','ekhtelaf masahat = ', dayereh(r) - mostatil(w,l))

##ekhtelaf()




##dars
a = 'mohamad'
##s = 'salam {:^10} halet chetoreh emruz {:.1%} ast'.format(a,23.54345)
##s = 'salam {:^20} halet chetoreh emruz {:%} ast'.format(a,23.54345)
##s = 'salam {:^10} halet chetoreh emruz {:,} ast'.format(a,2354345345)
s = 'salam {:<10} halet chetoreh emruz {:.3e} ast'.format(a,2345.54345345)
##s = 'salam {:r>15} halet chetoreh emruz {:*>20.0f} ast'.format(a,23.54345345)


d = {1:'salam', 'ali':[1,2,3],(1,2,3): True,'reza':'fkjdskfjsk'}
##print(d.keys())
##print(d.items())
##print(d.values())

##z = tuple(d.items())
##print(z)

##print(d.popitem())
##print(d)

##z = d.pop('ali')
##print(z)
##print(d)



##d = {1:'salam', 'ali':[1,2,3],(1,2,3): True,'reza':'fkjdskfjsk'}
##keys = (5,4,'gdfgtgdf')
##values = ('gkdg',True,56)
##z = zip(keys,values)
##for key,value in z:  #tarkib 2 dictionary
##    d[key] = value
##print(d)
##    


d = dict(b=99,a=3,d=55,c=46)
a = sum(d.values())
z = sorted(d)


##d1 = {1:'salam', 'ali':[1,2,3],(1,2,3): True,'reza':'fkjdskfjsk','b':33}
##d2 = dict(b=99,a=3,d=55,c=46)
##d3 = { **d1, **d2}  



# d = {9:{('salam',4):54,'ali':{'world':[1,2,3],(1,2,3): True,'reza':'fkjdskfjsk'}}}
#
# z = d[9]['ali'][(1,2,3)]  #address True
# print(z)
