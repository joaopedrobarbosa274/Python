n = int(input("Digite o valor de n: "))


if n <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    count = 0  
    i = 1      

    while count < n:
        print(i)
        i += 2  
        count += 1
