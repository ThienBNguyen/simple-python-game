import random


def string_combine(aug):
    intro_text = 'subscribe to '
    return intro_text + aug


# def random_number_game():
#     random_number = random.randint(1, 100)
#     user_number = int(input('please guess a number that match with the computer'))
#     while user_number == random_number:
#         if random_number == user_number:
#             print('your are correct')
#         elif random_number < user_number:
#             print('your number is greater than computer number')
#         elif random_number > user_number:
#             print('your number is less than computer number')
#         return random_number


def user_guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x}: '))
        if guess < random_number:
            print('sorry, guess again.too low.')
        elif guess > random_number:
            print('sorry, guess again. too hight.')
    print(f'correct. {random_number}')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'is {guess} too high(H) , too low(L) or correct(C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'yay the computer guessed your, {guess}, correctly!!')


computer_guess(10)