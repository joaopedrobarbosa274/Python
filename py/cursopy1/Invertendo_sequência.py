numeros = []  

while True:
    numero = int(input("Digite um número: "))  
    if numero == 0:
        break  
    numeros.append(numero)  
for num in reversed(numeros):
    print(num)
