import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_prime_number(user_name):
    attempts = 0
    while attempts < 3:
        rundom_number = randint(1, 15)
        counter = 0
        print(f'Question: {rundom_number}')

        for i in range(2, rundom_number // 2 + 1):
            if rundom_number % i == 0:
                counter += 1
        if counter <= 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            attempts += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
