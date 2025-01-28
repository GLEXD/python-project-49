import prompt
from brain_games.scripts import consts


def run_game(description, get_question_and_answer):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}')
    print(description)
    for _ in range(consts.rounds):
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}')")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
