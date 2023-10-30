#!/usr/bin/env python3
import sys

sys.path.append("/home/barbpro/project1/python-project-49/brain_games/")

import prompt
from games.brain_calc import solve_exp


def main():
    print("Welcome to the Brain Games")

    user_name = prompt.string("May I have your name? ")

    print(f"Hello, {user_name}!")

    print("What is the result of the expression?")

    solve_exp()

    solve_exp()

    solve_exp()

    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
