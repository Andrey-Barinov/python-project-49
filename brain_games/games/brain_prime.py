from random import randint


def is_prime(number):
    if number == 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_round():
    random_num = randint(1, 100)

    question = f"Question: {random_num}"

    correct_answer = "yes" if is_prime(random_num) else "no"

    return question, correct_answer
