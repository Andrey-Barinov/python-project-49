from random import randint, choice


GAME_TASK = "What is the result of the expression?"


def calculate(num1, op, num2):
    res = eval(str(num1) + op + str(num2))
    return res


def game_round():
    random_num1 = randint(1, 20)

    random_num2 = randint(1, 20)

    ops = ["+", "-", "*"]

    random_op = choice(ops)

    question = f"Question: {random_num1} {random_op} {random_num2}"

    correct_answer = str(calculate(random_num1, random_op, random_num2))

    return question, correct_answer
