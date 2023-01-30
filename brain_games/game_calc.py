import random
import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def question(user_name):
    attempts = 0
    operator = ('-', '+', '*')
    choice_operator = random.choice(operator)

    while attempts < 3:
        random_number1 = randint(1, 10)
        random_number2 = randint(1, 10)
        dif_question = f'Question: {random_number1} {choice_operator} {random_number2}'
        print(dif_question)
        user_answer = prompt.string('Your answer: ')
        if choice_operator == '-':
            correct_answer = random_number1 - random_number2
        elif choice_operator == '+':
            correct_answer = random_number1 + random_number2
        else:
            correct_answer = random_number1 * random_number2
        if user_answer == str(correct_answer):
            print('Correct!')
            attempts += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. "
                  f"\nLet's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
