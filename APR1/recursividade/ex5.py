"""Escreva um algoritmo recursivo para retornar
a quantidade de caracteres de uma string."""

def count_chars(string):
    if string == "":
        return 0
    else:
        return 1 + count_chars(string[1:])

text = "test"
print(f"'{text}' has {count_chars(text)} chars.")

