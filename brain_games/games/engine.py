import prompt


def run(game):
    print("Welcome to the Brain Games")

    user_name = prompt.string("May I have your name? ")

    print(f"Hello, {user_name}!")

    print(f"{game.game_task}")

    for round in range(1, 4):
        (question, correct_answer) = game.game_round()

        print(f"Question: {question}")

        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print("Correct!")

        else:
            print(
                f"{answer} is wrong answer ;(. "
                f"Correct answer was {correct_answer}."
            )

            print(f"Let's try again, {user_name}!")

            exit()

    print(f"Congratulations, {user_name}!")
