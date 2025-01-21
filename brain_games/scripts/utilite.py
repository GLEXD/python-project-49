from random import randint, choice


def get_random_number():
    return randint(1, 99)


def get_random_progression_index():
    return randint(0, 9)


def get_random_operation():
    return choice(['+', '-', '*'])
