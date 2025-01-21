from utilite import get_random_number
import prompt


def run_prime_game():
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    wins = 0
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\nAnswer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        answer = ""
        number = get_random_number()
        if is_prime(number):
            answer = "yes"
        else:
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
    run_prime_game()
