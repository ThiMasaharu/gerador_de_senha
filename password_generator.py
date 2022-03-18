import functions


functions.show_header()

# input of total letters, numbers and symbols in the password
total_letters = functions.totalize_quantity(f'\033[30;47mHow many letters do you want in your password?\033[m\n')
total_numbers = functions.totalize_quantity(f'\033[30;47mHow many numbers do you want in your password?\033[m\n')
total_symbols = functions.totalize_quantity(f'\033[30;47mHow many symbols do you want in your password?\033[m\n')

print(f'\033[7mWhat kind of password do you want to create?\033[m')
print(f'\033[1;36m 1 - for \"Letters then Numbers then Symbols\" sorted password\033[m')
print(f'\033[1;36m 2 - for random sorted password\033[m')

# input of which option the user wants
option = functions.select_option(f'\033[1;33mYour option: \033[m')

# generating password according to selected option
password = functions.generate_password(option, total_letters, total_numbers, total_symbols)

print(f'\033[1;33mPassword generated is: \033[m{password}')
