digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
phone = input("phone: ")

output = ""
for x in phone:
    output += digits_mapping.get(x,"!") + " "
print(output)


