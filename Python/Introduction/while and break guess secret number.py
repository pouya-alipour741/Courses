# secret_number = 9
# guess_count=0
# guess_limit=3
# while guess_count < guess_limit:
#     guess_count= guess_count + 1
#     guess = int(input('guess: '))
#     if secret_number == guess:
#      print('you win')
#      break
# else:
#      print("you failed !")

 #my version
secret_number = 5
digits_mapping = {
    1: "first",
    2: "second",
    3: "third",
}
max_guess = 3
guess_count = 0
guess = 0
print('guess a number between 1 to 9')
while guess_count != 3 and guess != 5:
    try:
        while guess_count < max_guess:
            guess_count += 1
            guess = int(input(f'{digits_mapping.get(guess_count)} guess :'))
            if secret_number == guess:
                print('correct\thooray!')
                break
            elif guess_count < 3:
                print('try again')
        else:
            print('you failed')

    except ValueError:
        if guess_count == 3:
            print('you Failed')
        else:
            print('you must type a number')
if __name__ == '__main__':
    pass
else:
    print('\nrunning indirectly')






























