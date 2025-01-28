from brain_games.utilite import get_random_number
from brain_games.consts import DESCRIPTION_PRIME
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


def start_game():
    engine.run_game(DESCRIPTION_PRIME, get_question_and_answer)
