import pandas as p

dados = {
'nome':['Ana', 'bruno'],
'idade':[23, 35,]

}

df= p.DataFrame(dados)

for id, row in df.iterrows():
    print(f'in: {id}, nome: {row["nome"]}, idade{row["idade"]}')