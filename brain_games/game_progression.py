import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_progression(user_name):
    attempts = 0
    while attempts < 3:
        first_element = randint(2, 20)
        num_element = 10
        step = randint(2, 6)
        last_element = first_element + num_element * step
        miss_element = randint(0, num_element - 1)

        list_elements = list(range(first_element, last_element, step))

        right_answer = str(list_elements[miss_element])

        list_elements[miss_element] = '..'

        question = 'Question: '

        for element in list_elements:
            question += str(element) + ' '
        print(question)

        user_answer = prompt.string('Your answer: ')

        if user_answer == right_answer:
            print('Correct!')
            attempts += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
