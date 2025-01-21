import prompt
from utilite import get_random_number

def run_game():
    wins = 0
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\nAnswer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = get_random_number()
        answer = ""
        if number % 2 == 0:
            answer = "yes"
        if number % 2 != 0:
            answer = "no"
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")
        if answer == user_answer:
            print("Correct!")
            wins += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
            break
        if wins == 3:
            print(f"Congratulations, {name}!")
            break


if __name__ == '__main__':
    run_game()
