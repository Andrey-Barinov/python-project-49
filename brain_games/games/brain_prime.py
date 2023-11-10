from random import randint


GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


def game_round():
    random_num = randint(1, 100)

    question = f"Question: {random_num}"

    correct_answer = "yes" if is_prime(random_num) else "no"

    return question, correct_answer
