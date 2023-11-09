from random import randint


def is_even(num):
    return num % 2 == 0


game_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_round():
    random_num = randint(1, 100)

    question = f"Question: {random_num}"

    correct_answer = "yes" if is_even(random_num) else "no"

    return question, correct_answer
