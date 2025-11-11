"""Faça uma função recursiva para calcular o
resto da divisão inteira."""

def module(number, divisor):
    if number < divisor:
        return number
    else:
        return module(number-divisor, divisor)

number =int(input("number: "))
divisor = int(input("divisor: "))
print(module(number, divisor))