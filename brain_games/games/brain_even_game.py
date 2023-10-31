import prompt
from random import randint


def ask_is_num_even(user_name):
    random_number = randint(1, 100)

    print(f"Question: {random_number}")

    answer = prompt.string("Your answer: ")

    if answer == "yes":
        if random_number % 2 == 0:
            print("Correct!")

        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")

            print(f"Let's try again, {user_name}!")

            exit()

    elif answer == "no":
        if random_number % 2 != 0:
            print("Correct!")

        else:
            print("'no' is wrong answer ;(. Correct answer was 'yes'")

            print(f"Let's try again, {user_name}!")

            exit()

    else:
        print("incorrect answer! You should write 'yes' or 'no'.")

        print(f"Let's try again, {user_name}!")

        exit()
