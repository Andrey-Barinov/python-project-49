import prompt
from random import randint, choice

user_name = ""


def solve_exp():
    ops = ["+", "-", "*"]

    random_op = choice(ops)

    random_num1 = randint(1, 20)

    random_num2 = randint(1, 20)

    result_of_expr = eval(str(random_num1) + random_op + str(random_num2))

    print(f"Question: {random_num1}{random_op}{random_num2}")

    answer = prompt.string("Your answer: ")

    if answer == str(result_of_expr):
        print("Correct!")

    else:
        print(
            f"""{answer} is wrong answer ;(.
            Correct answer was {result_of_expr}."""
        )

        print(f"Let's try again, {user_name}!")

        exit()
