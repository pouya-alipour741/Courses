# do you know how to make a loop where it ask an user input production per day and increases 1 day in the question, for example ("Enter production at day 1) then each time it ask it changes to 2,3,4,5. Is this possible?


# i = 0
# while i < 5 :
#     i += 1
#     command = input(f'enter production at day {i} :')
#     print(command)
#
# for i in range(1, 6):
#
#    production = input("Enter production at day " + str(i) + ": ")
#    print(production)
#

#how to make a sum of products ? solved!
output = 0
for i in range(11,13):
    for d in range(1,3):
        production = input(f'production at month/day {i},{d}:')
        output += int(production)
print(output)




