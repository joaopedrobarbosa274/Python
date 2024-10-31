'''
a) Use uma variável para representar o nome de uma pessoa e imprima uma mensagem para essa pessoa. Sua mensagem deve ser simples, como “Olá Eric, gostaria de aprender um pouco de Python hoje?”

b) Use uma variável para representar o nome de uma pessoa e, em seguida, imprima o nome dessa pessoa com todas as letras minúsculas. Na sequência, imprima todas as letras maiúsculas e, por fim, apenas as iniciais de cada palavra em maiúscula.

c) encontre uma citação de uma pessoa famosa que você admira. Imprima a citação e o nome de seu autor. Sua saída deve ser algo como o seguinte, "incluindo as aspas":

*Albert Einstein disse uma vez: “Uma pessoa que nunca cometeu um erro nunca tentou nada novo”.*
d) Repita o Exercício "c", mas desta vez, represente o nome da pessoa famosa usando uma variável chamada pessoa_famosa. Em seguida, refaça a composição de sua mensagem e represente-a com uma nova variável chamada mensagem. Imprima sua mensagem.

e) Use uma variável para representar o nome de uma pessoa e inclua alguns caracteres de espaço em branco no início e no final do nome. Certifique-se de usar cada uma das combinações de caracteres "\t" e "\n" pelo menos uma vez.

f) Imprima o nome armazenado na atividade "e" uma vez, para que o espaço em branco ao redor do nome seja exibido. Em seguida, imprima o nome usando cada uma das três funções de remoção, lstrip(), rstrip() e strip().

g) Atribua o valor python_notes.txt a uma variável chamada nome_arquivo. Em seguida, programe um método para exibir o nome do arquivo sem a extensão do arquivo, como fazem alguns navegadores de arquivos.
'''
#A)
nome = input("digite o seu nome: ")


print("Olá,",nome, "gostaria de aprender um pouco de Python hoje?")

#B)
print(nome.lower())
print(nome.upper())
print(nome.title())

#c)
citacao = '"A persistência é o caminho do êxito."'
autor = "Charles Chaplin"


print(citacao + " - " + autor)

#D)
citacao = '"A persistência é o caminho do êxito."'
pessoa_famosa = "Charles Chaplin"

mensagem = citacao + " - " + pessoa_famosa


print(mensagem)

#E)
nome = "\t   João da Silva   \n"
print("Nome original:", nome)

nome_limpo = nome.strip()
print("Nome sem espaços em branco:", nome_limpo)

#F)
nome = "\t   João da Silva   \n"
print("Nome original com espaços:")
print(nome)  

nome_limpado_esquerda = nome.lstrip()
print("Nome sem espaços à esquerda:")
print(nome_limpado_esquerda)

nome_limpado_direita = nome.rstrip()
print("Nome sem espaços à direita:")
print(nome_limpado_direita)

nome_limpado = nome.strip()
print("Nome sem espaços de ambos os lados:")
print(nome_limpado)

#G) 
nome_arquivo = "python_notes.txt"

def nome_sem_extensao(arquivo):
    return arquivo.rsplit('.', 1)[0]

nome_sem_ext = nome_sem_extensao(nome_arquivo)
print("Nome do arquivo sem extensão:", nome_sem_ext)


