import prompt
import random
import math


def run_gcd_game():
    wins = 0
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\nFind the greatest common divisor of given numbers.')
    for _ in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f"Question: {num1} {num2}")
        user_answer = prompt.string("Your answer: ")
        correct_answer = math.gcd(num1, num2)
        if correct_answer == int(user_answer):
            print("Correct!")
            wins += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break
        if wins == 3:
            print(f"Congratulations, {name}!")
            break


if __name__ == '__main__':
    run_gcd_game()
