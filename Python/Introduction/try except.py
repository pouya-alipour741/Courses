try:
    age = int(input("age: "))
    income = int(input('income'))
    print(income / age)
except ZeroDivisionError:
    print('age can not be 0!')
except ValueError:
    print('invalid value')