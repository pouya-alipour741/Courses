#order to check > local enclosing global builtins


# x = 'global x'

# def test():
#     x = 'local x'
#     print(x)
#
# test()
# print(x)


# x = 'global x' # to change global value within the function but be careful not to overuse this because most likely you don't need this
#
#
# def test():
#     global x
#     x = 'local x'
#     print(x)
#
# test()
# print(x)


# def outer():
#     x = 'outer x'
#
#     def inner():
#         #nonlocal x # to change local x of our enclosing function ,this one gets more use than global x
#         x = 'inner x'
#         print(x)
#
#     inner()
#     print(x)
# outer()


x = 'global x'


def outer():
    x = 'outer x'

    def inner():
        # x = 'inner x'
        print(x)

    inner()
    print(x)
outer()
print(x)

