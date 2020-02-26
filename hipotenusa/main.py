from math import sqrt


def int_row_input(message):
    return [int(number_string) for number_string in input(message).split()]


a, b = int_row_input('Say me the cathetus sides: ')
c = sqrt(a**2 + b**2)
print(f'The hipotenuse is {c}')

