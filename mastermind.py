import random

LIVES = 10


def gen_code():
    code = []
    for item in range(4):
        code.append(random.randint(0, 9))
    return code


def prompt_guess():
    guess = input("Enter your four digit guess:")
    guess_list = []
    for number in guess:
        guess_list.append(int(number))
    return guess_list


def check_guess(code, guess):
    response = []
    for number in guess:
        if number in code:
            if guess.index(number) == code.index(number):
                response.append('R')
            else:
                response.append('Y')
        else:
            response.append('B')
    return response


hidden_code = gen_code()
print(hidden_code)

while LIVES > 0:
    player_guess = prompt_guess()
    if check_guess(player_guess, hidden_code) == ['R', 'R', 'R', 'R']:
        print(check_guess(player_guess, hidden_code))
        print('You win!')
        LIVES = 0
    else:
        print(check_guess(player_guess, hidden_code))
        LIVES -= 1


