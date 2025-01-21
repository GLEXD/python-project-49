import prompt
from utilite import get_random_number, get_random_operation


def get_random_expression():
    num1 = get_random_number()
    num2 = get_random_number()
    operation = get_random_operation()
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    return f"{num1} {operation} {num2}", correct_answer


def run_expressions_game():
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\nWhat is the result of the expression?')
    wins = 0
    for _ in range(3):
        question, correct_answer = get_random_expression()
        print("Question:", question)
        user_answer = prompt.string("Your answer: ")
        if int(user_answer) == correct_answer:
            print("Correct!")
            wins += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break
        if wins == 3:
            print(f"Congratulations, {name}!")
            break


if __name__ == '__main__':
    run_expressions_game()
