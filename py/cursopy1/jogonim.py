def computador_escolhe_jogada(n, m):
    
    for i in range(1, m + 1):
        if (n - i) % (m + 1) == 0:
            return i
    return min(m, n)

def usuario_escolhe_jogada(n, m):
    
    jogada = 0
    while jogada < 1 or jogada > m or jogada > n:
        jogada = int(input(f"Quantas peças você vai tirar? (1 a {min(m, n)}): "))
        if jogada < 1 or jogada > m or jogada > n:
            print("Oops! Jogada inválida. Tente de novo.")
    return jogada

def partida():
    
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    
    if n % (m + 1) == 0:
        print("Você começa!")
        vez_do_usuario = True
    else:
        print("Computador começa!")
        vez_do_usuario = False

   
    while n > 0:
        if vez_do_usuario:
            jogada = usuario_escolhe_jogada(n, m)
            print(f"Você tirou {jogada} peça(s).")
        else:
            jogada = computador_escolhe_jogada(n, m)
            print(f"O computador tirou {jogada} peça(s).")
        
        n -= jogada
        print(f"Agora restam {n} peça(s) no tabuleiro.\n")
        vez_do_usuario = not vez_do_usuario

    
    if vez_do_usuario:
        print("O computador ganhou!")
    else:
        print("Você ganhou!")

def campeonato():
   
    print("Você escolheu um campeonato!")
    placar_computador = 0
    placar_usuario = 0

    for rodada in range(1, 4):
        print(f"**** Rodada {rodada} ****")
        partida()
        if "O computador ganhou!" in globals()['__last_result']:
            placar_computador += 1
        else:
            placar_usuario += 1
    
    print("**** Final do campeonato! ****")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    escolha = 0
    while escolha != 1 and escolha != 2:
        escolha = int(input())

    if escolha == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    else:
        campeonato()

if __name__ == "__main__":
    main()
