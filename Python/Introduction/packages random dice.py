import random
#my solution
# class Dice:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def roll(self):
#         print(f'({self.x},{self.y})')

# dice = Dice(random.randint(1,6),random.randint(1,6))
# dice.roll()

# how the guide solved
class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second

dice = Dice()
print(dice.roll())








