"""Faça uma função recursiva para encontrar a
potência positiva (n>=0) de um número X. """

def pow(number, power):
    if power == 1:
        return number
    else:
        return number * pow(number, power-1)
    
number =int(input("number: "))
power = int(input("power: "))
print(pow(number, power))