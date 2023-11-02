#!/usr/bin/env python3
import sys

sys.path.append("/home/barbpro/project1/python-project-49/brain_games/")

import prompt
from games.brain_prime import ask_is_num_prime


def main():
    print("Welcome to the Brain Games")

    user_name = prompt.string("May I have your name? ")

    print(f"Hello, {user_name}!")

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    ask_is_num_prime(user_name)

    ask_is_num_prime(user_name)

    ask_is_num_prime(user_name)

    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
