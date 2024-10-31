# Função que verifica se um número é primo
def éPrimo(k):
    if k < 2:
        return False
    i = 2
    while i * i <= k:  # Continua enquanto i² for menor ou igual a k
        if k % i == 0:  # Verifica se k é divisível por i
            return False  # Não é primo se for divisível
        i += 1  # Incrementa i
    return True  # Se não encontrou divisores, é primo

# Função que retorna o maior número primo menor ou igual a n
def maior_primo(n):
    while n >= 2:  # Continua enquanto n for maior ou igual a 2
        if éPrimo(n):  # Verifica se n é primo
            return n  # Retorna n se for primo
        n -= 1  # Decrementa n em 1

# Exemplos de execução
print(maior_primo(100))  # Saída: 97
print(maior_primo(7))    # Saída: 7