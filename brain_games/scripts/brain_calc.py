#!/usr/bin/env python3
import prompt
from brain_games.games.brain_calc import solve_exp


def main():
    print("Welcome to the Brain Games!")

    user_name = prompt.string("May I have your name? ")

    print(f"Hello, {user_name}!")

    print("What is the result of the expression?")

    solve_exp(user_name)

    solve_exp(user_name)

    solve_exp(user_name)

    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
