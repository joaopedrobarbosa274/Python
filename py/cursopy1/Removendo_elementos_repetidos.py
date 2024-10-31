def remove_repetidos(lista):
    lista_sem_repetidos = list(set(lista))
    lista_sem_repetidos.sort()
    return lista_sem_repetidos
lista = [2, 4, 2, 2, 3, 3, 1]
print(remove_repetidos(lista))
print(remove_repetidos([1, 2, 3, 3, 3, 4]))

