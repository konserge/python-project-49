import prompt
from random import randint



def welcome_user():
    name = prompt.string('May I have your name? ')
    name = prompt.string(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

def question():
    random_number = randint(1, 100)
    print(f'Question: {random_number}')
    user_answer = prompt.string('Your answer: ')

def correct_answer():
    if (user_answer == 'yes' and random_number % 2 == 0) or (user_answer == 'no' and random_number % 2 != 0):
        return 'Correct!'
    elif user_answer == 'yes' and random_number % 2 != 0:
        return f"'yes' is wrong answer ;(. Correct answer was 'no'. \n Let's try again, {user_name}!"
    elif user_answer == 'no' and random_number % 2 == 0:
        return f"'no' is wrong answer ;(. Correct answer was 'yes'. \n Let's try again, {user_name}!"



    start = 0
    attempt = 3
    random_number = randint(1, 100)

    while start <= attempt:
        start += 1


if __name__ == '__main__':
    main()
