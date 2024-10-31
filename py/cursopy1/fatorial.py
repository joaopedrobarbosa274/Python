def fatorial(n):
    if n == 0:
        return 1 
    resultado = 1
    i = 1
    while i <= n:
        resultado *= i
        i += 1
    return resultado


n = int(input("Digite o valor de n: "))


if n < 0:
    print("Por favor, insira um número natural (não negativo).")
else:
 
    print(fatorial(n))
