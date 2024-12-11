import prompt
import random


# def find_gcd():
#     num1 = random.randint(1, 100)
#     num2 = random.randint(1, 100)
#     question = print(num1, num2)
#     while num1 != 0 and num2 != 0:
#         if num1 > num2:
#             num1 = num1 % num2
#         else:
#             num2 = num2 % num1
#     return num1 + num2, question


def run_gcd_game():
    wins = 0
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\nFind the greatest common divisor of given numbers.')
    for _ in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        while num1 != 0 and num2 != 0:
            if num1 > num2:
                num1 = num1 % num2
            else:
                num2 = num2 % num1
        correct_answer = num1 + num2
        print(f"Question:{num1} {num2}")
        user_answer = prompt.string("Your answer: ")
        if correct_answer == user_answer:
            print("Correct!")
            wins += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break
        if wins == 3:
            print(f"Congratulations, {name}!")
            break