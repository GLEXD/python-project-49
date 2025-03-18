from brain_games.utilite import get_random_number
from brain_games.consts import description_prime
from brain_games import engine


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_question_and_answer():
    problem_number = get_random_number()
    answer = "yes" if is_prime(problem_number) else "no"
    return problem_number, answer


def start_prime_game():
    engine.run_game(description_prime, get_question_and_answer)
