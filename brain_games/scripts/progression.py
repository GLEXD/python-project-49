import prompt
from utilite import get_random_number, get_random_progression_index


def generate_progression():
    length = get_random_number()
    first = get_random_number()
    step = get_random_number()
    progression = [first + i * step for i in range(length)]
    missing_index = get_random_progression_index()
    missing_number = progression[missing_index]
    progression[missing_index] = '..'
    return progression, missing_number


def run_progression_game():
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\nWhat number is missing in the progression?')
    wins = 0
    for _ in range(3):
        progression, missing_number = generate_progression()
        print("Question:", ' '.join(map(str, progression)))
        user_answer = prompt.string("Your answer: ")
        if int(user_answer) == missing_number:
            print("Correct!")
            wins += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{missing_number}'.\nLet's try again, {name}!")
            break
        if wins == 3:
            print(f"Congratulations, {name}!")
            break


if __name__ == '__main__':
    run_progression_game()
