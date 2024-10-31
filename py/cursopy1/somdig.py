num = int(input("Digite um número inteiro: "))
soma_digitos = 0 

while num > 0:
    digito = num % 10  
    soma_digitos += digito  
    num = num // 10  


print(soma_digitos)

