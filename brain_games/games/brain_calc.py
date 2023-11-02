import prompt
from random import randint, choice


def solve_exp(user_name):
    ops = ["+", "-", "*"]

    random_op = choice(ops)

    random_num1 = randint(1, 20)

    random_num2 = randint(1, 20)

    result_of_exp = eval(str(random_num1) + random_op + str(random_num2))

    print(f"Question: {random_num1} {random_op} {random_num2}")

    answer = prompt.string("Your answer: ")

    if answer == str(result_of_exp):
        print("Correct!")

    else:
        print(
            f"{answer} is wrong answer ;(."
            f"Correct answer was {result_of_exp}."
        )

        print(f"Let's try again, {user_name}!")

        exit()
