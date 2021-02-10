#jogo da velha simplificado e com funcões adicionais
import random
O = 'O'
VAZIO = ''
jogador = 'X'
pontos = 0
tabuleiro = [VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO]

vencedor = False
resposta = ''
while True:

    print(' ==== Jogo da velha ====')
    print(' - - - Jogador X - - -')
    print(f'Pontos X = {pontos}')

    #imprimir tabuleiro
    for i in range(0,9,3):
        if i <= 8:
            print(f'{i} | {i+1} |  {i+2}  ')


    #preencher tabualeiro
    print()
    casa = int(input('Digite em qual número deseja jogar :'))
    while tabuleiro[casa] != VAZIO:
        print("Jogada invalida esta casa já possui um valor ")
        casa = int(input("Escolha a casa onde deseja jogar"))
    tabuleiro[casa] = jogador
    Comp = random.randint(0,8)
    for i in range(9):
        if tabuleiro[i] == VAZIO:
            tabuleiro[Comp] = O

    for i in range(0,9,3):
        print(f' _{tabuleiro[i]}_  |   _{tabuleiro[i+1]}_    |   _{tabuleiro[i+2]}_')

    # condição para o jogador ganhar na horizontal:
    for i in range(0,9,3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != VAZIO:
            vencedor = tabuleiro[i]

    #condição para o jogador ganhar na vertical:
    if not vencedor:
        for i in range(3):
            if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+3] != VAZIO :
                vencedor = tabuleiro[i]

    #condição para ganhar na diagonal:
    if not vencedor:
        for i in range(0,3,2):
            if tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i] != VAZIO:
                vencedor = tabuleiro[i]



    #condição fim de jogo
    if vencedor:
        print(f'Vencedor = {vencedor}')
        if vencedor == 'X':
            pontos += 1
        else:
            vencedor == 'O'
        resposta = input('Deseja Jogar Novamente? [S]Sim/[N]Não').upper().strip()
        if resposta == "S":
            tabuleiro.clear()

        else:
            break
    #condição de empate
    else:
        if not VAZIO in tabuleiro:
            print('Empate ! Deu Velha !!')
            resposta = input('Deseja Jogar Novamente? [S]Sim/['
                             'N]Não').upper().strip()
            if resposta == "S":
                tabuleiro.clear()

            else:
                break
