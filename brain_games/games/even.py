from brain_games.utilite import get_random_number
from brain_games.consts import description_even
from brain_games import engine


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    number = get_random_number()
    answer = "yes" if is_even(number) else "no"
    return number, answer


def run_even_game():
    engine.run_game(description_even, get_question_and_answer)
