numero = input("Digite um número inteiro: ")
i = 0
digito_adjacente = False  

while i < len(numero) - 1:  
    if numero[i] == numero[i + 1]:  
        digito_adjacente = True  
        break  
    i += 1  

if digito_adjacente:
    print("sim")
else:
    print("não")
