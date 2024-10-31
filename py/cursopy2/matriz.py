def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []
    for l in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz


matriz = cria_matriz(6, 8, 4)
print(matriz)
