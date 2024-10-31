'''
nome = input("nome: ")
print("comprimento do seu nome:", len(nome))
'''
'''
def imc():
    peso = int(input("digite seu peso: "))
    altura = float(input("digite sua altura: "))
    imc = peso / (altura**2)
    return imc

resultado = imc()
print("seu imc é: ", resultado)
'''
def calc():
    pessoas = int(input("Digite quantas pessoas: ")) 
    valor = float(input("Digite o valor da conta: "))

    mda_p_pessoa = valor / pessoas
    
    gorjeta = mda_p_pessoa * 0.1
    
    total_por_pessoa = mda_p_pessoa + gorjeta
   
    print(f"O valor por pessoa: R$ {mda_p_pessoa:.2f}")
    print(f"Gorjeta: R$ {gorjeta:.2f}")
    print(f"Total por pessoa (com gorjeta): R$ {total_por_pessoa:.2f}")
    
    return total_por_pessoa

resultado = calc()
