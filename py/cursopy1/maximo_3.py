def maximo(x, y, z):
    if (x >= y) and (x >= z):  
        return x
    elif (y >= x) and (y >= z):  
        return y
    elif (z >= x) and (z >= y):
        return z
    else:
        return "Erro"  

print(maximo(10, 10, 10))  
print(maximo(0, -1, 1))    