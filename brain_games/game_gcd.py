from random import randint
import prompt
from math import gcd

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_gcd(user_name):
    attempts = 0

    while attempts < 3:
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        print(f'Question: {num_1} {num_2}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = gcd(num_1, num_2)
        # if num_1 < num_2:
        #     num_1, num_2 = num_2, num_1
        #     remainder_division = num_1 % num_2
        # else:
        #     remainder_division = num_1 % num_2
        # while remainder_division != 0:
        #     num_1 = num_2
        #     num_2 = remainder_division
        #     remainder_division = num_1 % num_2
        #     correct_answer = num_2
        if user_answer == str(correct_answer):
            print('Correct!')
            attempts += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. "
                  f"\nLet's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
