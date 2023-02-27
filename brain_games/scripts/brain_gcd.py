#!/usr/bin/env python3
from brain_games.game_gcd import welcome_user
from brain_games.game_gcd import get_gcd


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    get_gcd(name)


if __name__ == '__main__':
    main()
