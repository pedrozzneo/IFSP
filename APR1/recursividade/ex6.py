"""Crie uma função recursiva que exiba
verticalmente uma string"""

def exibir_vertical(string):
    if string == "":
        return
    print(string[0])
    exibir_vertical(string[1:])

string = "test"
exibir_vertical(string)
