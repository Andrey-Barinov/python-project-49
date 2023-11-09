from random import randint


def generate_progr(start, generator):
    progression = [str(start)]

    next_num = start + generator

    progression.append(str(next_num))

    i = 0

    while i < 10:
        next_next_num = next_num + generator

        next_num = next_next_num

        progression.append(str(next_next_num))

        i += 1

    return progression


game_task = "What number is missing in the progression?"


def game_round():
    random_num_start = randint(1, 20)

    generator_of_progr = randint(2, 5)

    random_index_replace = randint(0, 11)

    progression = generate_progr(random_num_start, generator_of_progr)

    correct_answer = progression[random_index_replace]

    progression[random_index_replace] = ".."

    question = f"Question: {' '.join(progression)}"

    return question, correct_answer
