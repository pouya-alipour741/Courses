name = input("name ?")
if len(name) < 3:
    print("name must be at least 3 charactors ! ")
elif len(name) > 20:
    print("name must be at most 20 charactors ")
else:
    print("everything looks good")