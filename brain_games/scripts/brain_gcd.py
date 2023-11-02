#!/usr/bin/env python3
import prompt
from brain_games.games.brain_gcd import ask_to_find_gcd


def main():
    print("Welcome to the Brain Games!")

    user_name = prompt.string("May I have your name? ")

    print(f"Hello, {user_name}!")

    print("Find the greatest common divisor of given numbers.")

    ask_to_find_gcd(user_name)

    ask_to_find_gcd(user_name)

    ask_to_find_gcd(user_name)

    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
