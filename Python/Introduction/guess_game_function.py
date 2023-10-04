#class method
# class Game:
#     def __init__(self,x):
#         self.secret_number = x
#     def guessing_game(self):
#         digits_mapping = {
#             1: "first",
#             2: "second",
#             3: "third",
#         }
#         max_guess = 3
#         guess_count = 0
#         guess = 0
#         print('guess a number between 1 to 9')
#         while guess_count < max_guess :  #and guess != self.secret_number
#             try:
#                 guess_count += 1
#                 guess = int(input(f'{digits_mapping.get(guess_count)} guess :'))
#                 if self.secret_number == guess:
#                     print('correct\thooray!')
#                     break
#                 elif guess_count < 3:
#                     print('try again')
#             except ValueError:
#                 if guess_count == 3:
#                     print('You Failed')
#                     break
#                 else:
#                     print('must choose a number between 1-9')
#         else:
#             print('you failed')
#
# g1 = Game(5)
# g1.guessing_game()

#class method 2 better version
# class GuessNumber:
#     def __init__(self,sec_guess):
#         self.hads = sec_guess
#
#
#     def guess_number_max(self,max_guess):
#         guess_count = 0
#         guess = 1
#         digits_mapping = {0:'first',
#                           1:'second',
#                           2: 'third',
#                           3:'fourth',
#                           4: 'fifth'}
#         while guess_count < max_guess and guess != self.hads:
#             try:
#                 guess = int(input(f"your {digits_mapping.get(guess_count,'a')} guess ,choose a number between 1 to 10 .you have {max_guess - guess_count } chance left > "))
#                 guess_count += 1
#                 if guess == self.hads:
#                     print('nice!')
#                     break
#                 elif guess != self.hads and guess_count < max_guess:
#                     print('try again')
#
#             except ValueError:
#                 if guess_count < max_guess:
#                     print('you must guess a number!')
#                 else:
#                     print('you failed')
#         else:
#             print('you lost')
#
#
# g1 = GuessNumber(10)
# g1.guess_number_max(4)

#function version
def guessing_game(max_guess = 3,secret_num = 0):
    guess_count = 0
    digits_mapping = {0: 'first',
                      1: 'second',
                      2: 'third'}
    while guess_count < max_guess:
        try:
            print(f" your {digits_mapping.get(guess_count, 'n')} guess ,type a number between 1-10: ")
            guess = int(input('> '))
            guess_count += 1
            if guess == secret_num:
                print('you won')
                break
            elif guess != secret_num:
                print(f'{max_guess - guess_count} guess left')
        except ValueError:
            print('must type number')
            print(f'{max_guess - guess_count} guess left')
    else:
        print('you failed')

guessing_game(secret_num=2)




