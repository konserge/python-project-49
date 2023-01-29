#!/usr/bin/env python3

from brain_games.game import welcome_user
from brain_games.game import question


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    question(name)


if __name__ == '__main__':
    main()
