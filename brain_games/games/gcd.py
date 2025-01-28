from brain_games.utilite import get_random_number
from brain_games.consts import DESCRIPTION_GCD
import math
from brain_games import engine


def get_question_and_answer():
    number1, number2 = get_random_number(), get_random_number()
    correct_answer = str(math.gcd(number1, number2))
    question = f"{number1} {number2}"
    return question, correct_answer


def start_game():
    engine.run_game(DESCRIPTION_GCD, get_question_and_answer)
