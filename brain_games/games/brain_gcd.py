import prompt
from random import randint


def find_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2

        else:
            num2 = num2 % num1

    return num1 + num2


def ask_to_find_gcd(user_name):
    random_num1 = randint(1, 100)

    random_num2 = randint(1, 100)

    gcd = find_gcd(random_num1, random_num2)

    print(f"Question:{random_num1} {random_num2}")

    answer = prompt.string("Your answer: ")

    if answer == str(gcd):
        print("Correct!")

    else:
        print(
            f"{answer} is wrong answer ;(."
            f"Correct answer was {gcd}."
        )

        print(f"Let's try again, {user_name}!")

        exit()
