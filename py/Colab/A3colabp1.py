'''
nome = ['João' , 'Pedro' , 'Carol', 'Carolaine']
for n in nome:
    print("ola,", n)
'''
nome = ['João' , 'Pedro' , 'Carol', 'Carolaine']
print(nome[1])
nome[1] = 'Vasconcelos'
for n in nome:
    print("ola,", n)

nome.extend(['ads','Gonçalves','Lima'])
print(nome)
print(nome[2], "encontrei uma mesa")
nome.insert(0, 'tmj')
nome.insert(4,'a')
nome.append('nada')
for n in nome:
    print("ola,", n)

#D)