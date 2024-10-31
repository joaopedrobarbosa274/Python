n = int(input("Digite um número inteiro positivo: "))

if n <= 1:
    print("não primo")  
else:
    primo = True  
    i = 2  

    while i <= n // 2:  
        if n % i == 0:  
            primo = False  
            break 
        i += 1  

    
    if primo:
        print("primo")
    else:
        print("não primo")
