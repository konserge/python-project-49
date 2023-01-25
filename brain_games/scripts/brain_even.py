#!/usr/bin/env python3

from brain_games.game import welcome_user
from brain_games.game import question
from brain_games.game import correct_answer


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    question()
    correct_answer()


    # start = 0
    # attempt = 3


    # while start <= attempt:
    #     print('Welcome to the Brain Games!')
    #     user_name = prompt.string('May I have your name? ')
    #     print(f"Hello, {user_name}!")
    #     print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    #     print(f'Question: {random_number}')
    #     user_answer = prompt.string('Your answer: ')
    #     if (user_answer == 'yes' and random_number % 2 == 0) or (user_answer == 'no' and random_number % 2 != 0):
    #         print('Correct!')
    #     elif user_answer == 'yes' and random_number % 2 != 0:
    #         print(f"'yes' is wrong answer ;(. Correct answer was 'no'. \n Let's try again, {user_name}!")
    #     elif user_answer == 'no' and random_number % 2 == 0:
    #         print(f"'no' is wrong answer ;(. Correct answer was 'yes'. \n Let's try again, {user_name}!")
    #     start += 1

if __name__ == '__main__':
    main()
