#projeto Jogo da Velha
#desenvolvido por Rafael Maldivas

# ==== Módulos e importações ====
import random
import os
import time

#===== Variáveis Globais =====
limpa = "os.system('cls' if os.name == 'nt' else 'clear')"
jogando = 'X'
X = 0
O = 0
empate = 0
alinhamento = False
V = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


# ==== Interface do Jogo ====

def cabecalho():
    print('||==================================================================||')
    print('||                       JOGO DA VELHA                              ||')
    print('||==================================================================||')

def placar():
    print('||                           PLACAR                                 ||')
    print(f'||   [ O ] => {str(O)}                          {str(X)} <= [ X ]                 ||')
    print(f'||                         EMPATES  = > {str(empate)}                           ||')
    print('||==================================================================||')
    print(f'||                         JOGANDO => {str(jogando)}                             ||')
    print('||==================================================================||')

def velha():
    print('||                           +-----+-----+-----+                    ||')
    print(f'||                           |  {str(V[0][0])}  |  {str(V[0][1])}  |  {str(V[0][2])}  |                    ||')
    print('||                           +-----+-----+-----+                    ||')
    print(f'||                           |  {str(V[1][0])}  |  {str(V[1][1])}  |  {str(V[1][2])}  |                    ||')
    print('||                           +-----+-----+-----+                    ||')
    print(f'||                           |  {str(V[2][0])}  |  {str(V[2][1])}  |  {str(V[2][2])}  |                    ||')
    print('||                           +-----+-----+-----+                    ||')
    print('||==================================================================||')

# ==== Funcções Auxiliares ====
def jogador():
    return 'X' if random.randint(1,2) == 1 else 'O'

def jogou (msg):
    while True:
        try:
            jogada = input(msg)
            return int(jogada[0])
        except:
            print('Digite um valor aceito!!!')


def questao(msg, erro="Digite S para sim e N para não"):
    while True:
        try:
            r = input(msg).upper()
            if r[0] == 'S':
                return True
            elif r[0] == 'N':
                return False
            else:
                print(erro)
        except:
            print('Digite um valor aceito!!!')

# ========  Funções Principais ===========

def jogo_empate():

    for i in range(3):
        for j in range(3):
            if str(V[i][j]).isdigit():
                return False
    return True

def vitória():
    #horizontal
    if V[0][0] == V[0][1] == V[0][2]:
       alinhamento = True
    if V[1][0] == V[1][1] == V[1][2]:
       alinhamento = True
    if V[2][0] == V[2][1] == V[2][2]:
        alinhamento = True



#inicio do programa

inicio = True
while inicio:
    jogando = jogador()
    gameon = True

    while gameon:
        #cabeçalho

        eval(limpa); cabecalho();  placar(); velha()
        jogada = jogou("Jogue o número na posição desejada: ")

        #validação
        jogadaaceita  = False

        for i in range(3):
            for j in range(3):
                if jogada == V[i][j]:
                    V[i][j] = jogando
                    if V[i][j]
                    jogadaaceita = True


        if jogadaaceita:
            #verificar se jogo foi ganho ou empate
            vitória()
            if alinhamento == True:
                print(f'Jogador {jogando} ganhou')
            if jogo_empate():
                print('   Jogo Empatado   ')
                empate += 1
                time.sleep(3)
                gameon = False
                inicio = True if questao(' Deseja continuar ? (S/N)') else False

            else:
                jogando = "X" if jogando == 'O' else 'O'

        else:
            print("   Jogada Inválida   !!!   tente novamente")
            time.sleep(3)



        if not questao("Continuar? ([S]Sim/[N]Não)"):
            gameon = False
            inicio = False




