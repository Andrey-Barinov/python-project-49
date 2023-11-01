import prompt
from random import randint


def ask_to_find_num(user_name):
    random_num_start = randint(1, 20)

    generator_of_prog = randint(2, 5)

    random_index_replace = randint(0, 9)

    progression = [str(random_num_start)]

    next_num = random_num_start + generator_of_prog

    progression.append(str(next_num))

    i = 0

    while i < 10:
        next_next_num = next_num + generator_of_prog

        next_num = next_next_num

        progression.append(str(next_next_num))

        i += 1

    right_answer = progression[random_index_replace]

    progression[random_index_replace] = ".."

    print(f"Question: {' '.join(progression)}")

    answer = prompt.string("Your answer: ")

    if answer == right_answer:
        print("Correct!")

    else:
        print(f"{answer} is wrong answer ;(."
              f"Correct answer was {right_answer}.")

        print(f"Let's try again, {user_name}!")

        exit()
