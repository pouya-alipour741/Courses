weight = int(input('weight: '))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    weight = weight * 0.45
    print(f'you are {weight} kg ')
if unit.upper() == "K":
    weight = weight / 0.45
    print(f'you are {weight} pounds')



