from prompt_toolkit import prompt

def welcome_user():
    name = prompt('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
