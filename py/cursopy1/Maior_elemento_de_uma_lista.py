def maior_elemento(lista):
    if len(lista) == 0:
        return None  
    return max(lista)


print(maior_elemento([6, 2, 3]))  
print(maior_elemento([7, -7, 1, 5, 5, 7]))  
print(maior_elemento([-90, -27, -12]))  
print(maior_elemento([1])) 
