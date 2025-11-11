def fatorial(total, number):
    if number > 1:
        total *= number
        return fatorial(total, (number - 1))
    return total

total = 1
number = int(input("enter a number to calculate its fatorial: "))
print(f"fatorial of {fatorial(total, number)}")

#o valor de retorno do fatorial vai ser o valor de retorno do prox, e ai eu repito e vou atribuindo