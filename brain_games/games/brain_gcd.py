from random import randint


def find_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2

        else:
            num2 = num2 % num1

    return num1 + num2


game_task = "Find the greatest common divisor of given numbers."


def game_round():
    random_num1 = randint(1, 100)

    random_num2 = randint(1, 100)

    question = f"Question: {random_num1} {random_num2}"

    correct_answer = str(find_gcd(random_num1, random_num2))

    return question, correct_answer
