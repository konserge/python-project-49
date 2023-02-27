#!/usr/bin/env python3
from brain_games.game_progression import welcome_user
from brain_games.game_progression import get_progression


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What number is missing in the progression?')
    get_progression(name)


if __name__ == '__main__':
    main()