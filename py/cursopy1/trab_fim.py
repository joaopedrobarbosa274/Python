import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    similaridade = sum(abs(a - b) for a, b in zip(as_a, as_b)) / len(as_a)
    return similaridade

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    # Separar o texto em sentenças
    sentencas = separa_sentencas(texto)
    n_sentencas = len(sentencas)
    
    # Separar as sentenças em frases
    frases = []
    for sentenca in sentencas:
        frases.extend(separa_frases(sentenca))
    
    # Separar as frases em palavras
    palavras = []
    for frase in frases:
        palavras.extend(separa_palavras(frase))
    
    # Calcular as estatísticas
    n_palavras = len(palavras)
    tamanho_medio_palavra = sum(len(p) for p in palavras) / n_palavras if n_palavras else 0
    relacao_type_token = n_palavras_diferentes(palavras) / n_palavras if n_palavras else 0
    razao_hapax_legomena = n_palavras_unicas(palavras) / n_palavras if n_palavras else 0
    tamanho_medio_sentenca = sum(len(sentenca) for sentenca in sentencas) / n_sentencas if n_sentencas else 0
    complexidade_sentenca = len(frases) / n_sentencas if n_sentencas else 0
    tamanho_medio_frase = sum(len(frase) for frase in frases) / len(frases) if frases else 0
    
    return [tamanho_medio_palavra, relacao_type_token, razao_hapax_legomena, 
            tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    menor_similaridade = float('inf')
    texto_infectado = -1
    
    for i, texto in enumerate(textos):
        assinatura_texto = calcula_assinatura(texto)
        similaridade = compara_assinatura(assinatura_texto, ass_cp)
        
        if similaridade < menor_similaridade:
            menor_similaridade = similaridade
            texto_infectado = i + 1  # Para retornar 1 a n, não 0 a n-1

    return texto_infectado

# Execução do programa
if __name__ == "__main__":
    assinatura_coh_piah = le_assinatura()
    textos = le_textos()
    
    texto_infectado = avalia_textos(textos, assinatura_coh_piah)
    print(f"O autor do texto {texto_infectado} está infectado com COH-PIAH.")
