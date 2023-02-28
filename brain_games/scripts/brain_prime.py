#!/usr/bin/env python3
from brain_games.game_prime import welcome_user
from brain_games.game_prime import get_prime_number


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    get_prime_number(name)


if __name__ == '__main__':
    main()