from brain_games.game_calc import welcome_user
from brain_games.game_calc import question


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')
    question(name)


if __name__ == '__main__':
    main()
