#!/usr/bin/env python3
import sys

sys.path.append("/home/barbpro/project1/python-project-49/brain_games/")

import prompt
from brain_even_game import ask_is_num_even


def main():
    print("Welcome to the Brain Games")

    user_name = prompt.string("May I have your name? ")

    print(f"Hello, {user_name}!")

    print('Answer "yes" if the number is even, otherwise answer "no".')

    ask_is_num_even()

    ask_is_num_even()

    ask_is_num_even()

    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
