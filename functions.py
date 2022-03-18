import random
import string
from time import sleep


def show_header(): 
    """
    -> Show header of password generator 
    """
    print(f'\033[1m-\033[m'*60)
    print(f'\033[1mPassword Generator with Python\033[m'.center(60))
    print(f'\033[1m-\033[m'*60)


def totalize_quantity(user_input):
    """
    -> Function to get user input and return user input
    :param user_input: input of the value the user wants
    :return: return the value of user input
    """
    while True:
        sleep(0.6)
        try:
            total = int(input(user_input))
        except(ValueError, TypeError):
            print(f'\033[1;31mERROR! Type a valid integer!\033[m')
            continue
        else:
            return total


def select_option(user_input):
    """
    -> Function to get the user desired option for password
    :param user_input: input of the option the user wants
    :return: return which option the user selected
    """
    while True:
        user_option = totalize_quantity(user_input)
        if user_option==1 or user_option==2:
            return user_option
        else: 
            print(f'\033[1;31mERROR! Choose 1 or 2.\033[m')
            continue


def generate_password(option, letters, numbers, symbols):
    """
    -> function to generate password according to option and total of letters, numbers and symbols
    :param option: option user selected through select_option()
    :param letter: total amount of letters
    :param numbers: total amount of numbers
    :param symbols: total amount of symbols
    :return: returns letters+numbers+symbols password or random password
    """
    password = ''
    for i in range(0, letters):
        password += random.choice(string.ascii_letters)
    for i in range(0, numbers):
        password += random.choice(string.digits)
    for i in range(0, symbols):
        password += random.choice(string.punctuation)
    
    if option==1:   
        return password
    elif option==2:
        return ''.join(random.sample(password, len(password)))