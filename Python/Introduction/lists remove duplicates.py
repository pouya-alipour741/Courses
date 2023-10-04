numbers = [6,8,4,6,8,7,8]
unique = []
for item in numbers:
    if item not in unique:
        unique.append(item)
unique.sort()
print(unique)

