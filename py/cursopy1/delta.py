'''
import math
a= float(input("primeiro valor "))
b= float(input("segundo valor "))
c= float(input("terceiro valor "))
delta=float( b**2 - 4 * a *c)

if delta > 0:
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    print("As raízes reais são: x1 =",x1, "x2= ",  x2)
elif delta == 0:
    x = (-b) / (2 * a)
    print("A raiz real é: x = x", x)
else:
    parte_real = -b / (2 * a)
    parte_imaginaria = math.sqrt(-delta) / (2 * a)
    x1 = complex(parte_real, parte_imaginaria)
    x2 = complex(parte_real, -parte_imaginaria)
    print("As raízes complexas são: x1 =", x1, "x2 =", x2)

import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4 * a * c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    
    if x1 < x2:
        print("as raízes da equação são ", x1, "e", x2 )
    else:
        print("as raízes da equação são ", x2, "e", x1)
        
elif delta == 0:
    x = (-b) / (2 * a)
    print("a raiz dupla desta equação é ", x)
    
else:
    print("esta equação não possui raízes reais")
'''
import math

def delta(a, b, c):
    return b**2 - 4 * a * c

def main():
    a = float(input("digite o valor de a: "))
    b = float(input("digite o valor de b: "))
    c = float(input("digite o valor de c: "))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        print("a unica raiz é ", raiz1)

    else:
        if d < 0:
             print("essa equação não possui raizes reais")
        else:
             raiz1 = (-b + math.sqrt(d)) / (2 * a)
        raiz2 = (-b - math.sqrt(d)) / (2 * a)
        print("A primeira raiz é: ", raiz1)
        print("a segunda raiz é: ", raiz2)

