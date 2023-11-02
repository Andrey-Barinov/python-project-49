import prompt
from random import randint


def is_prime(num):
    if num in [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]:
        return "yes"
    else:
        return "no"


def ask_is_num_prime(user_name):
    random_num = randint(1, 100)

    right_answer = is_prime(random_num)

    print(f"Question: {random_num}")

    answer = prompt.string("Your answer: ")

    if answer == right_answer:
        print("Correct!")

    else:
        print(f"{answer} is wrong answer ;(."
              f"Correct answer was {right_answer}.")

        print(f"Let's try again, {user_name}!")

        exit()
