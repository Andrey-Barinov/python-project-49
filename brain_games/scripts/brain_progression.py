#!/usr/bin/env python3
import prompt
from games.brain_progression import ask_to_find_num


def main():
    print("Welcome to the Brain Games")

    user_name = prompt.string("May I have your name? ")

    print(f"Hello, {user_name}!")

    print("What number is missing in the progression?")

    ask_to_find_num(user_name)

    ask_to_find_num(user_name)

    ask_to_find_num(user_name)

    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
