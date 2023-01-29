import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def question(user_name):
    attempts = 0
    while attempts < 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')

        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if user_answer == correct_answer:
            print('Correct!')
            attempts += 1

        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. \nLet's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
