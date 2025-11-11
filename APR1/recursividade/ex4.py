"""Faça uma função recursiva para calcular o
MDC entre dois números x e y. Considere:
mdc(x; y) = y, se x >= y e x mod y = 0
 mdc(x; y) = mdc(y; x), se x < y
mdc(x; y) = mdc(y; x mod y), caso contrário"""

def mdc(x, y, divisor):
    if x % divisor == 0 and y % divisor == 0:
        return divisor
    else:
        return mdc(x, y, divisor-1)

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

if x < y:
    divisor = x
else:
    divisor = y

print(f"MDC({x}, {y}) = {mdc(x, y, divisor)}")
    