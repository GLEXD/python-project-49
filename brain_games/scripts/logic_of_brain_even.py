import prompt
import random
number = random.randint(1, 100)
def get_correct_answer():
    answer = ""
    if number % 2 == 0:
        answer = "yes"
    if number % 2 != 0:
        answer = "no"
    return answer
def run_game():
    name = prompt.string('''Welcome to the Brain Games!
May I have your name? ''')
    print(f"""Hello, {name}!
Answer "yes" if the number is even, otherwise answer "no".""")
    print(f"Question: {number}")
    user_answer = prompt.string("Your answer: ")
    if get_correct_answer() == user_answer:
        print("Correct!")
    else:
        print(f"""'{user_answer}' is wrong answer ;(. Correct answer was '{get_correct_answer()}'.
Let's try again, {name}!""")





run_game()

