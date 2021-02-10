import random
import emoji
from time import sleep
maria_beatriz = ['ana', 'aurora', 'elza', 'bela', 'moana', 'ariel', 'mulan', 'branca', 'tiana', 'merida', 'pocahontas',
                 'cinderela', 'alice', 'sininho', 'jasmin', 'rapunzel','olaf']
maria_dicas = ['Na verdade a princesa é a irmã dela', 'A mais dorminhoca das princesas', 'O frio não é problema pra essa princesa',
               'Ela descobriu que a beleza interior é melhor que a exterior', 'Um mar de aventuras', 'Gosta muito do fundo do mar',
               'A mais guerreira das princesas', 'alguma coisa de neve', 'beijou um sapo', 'guerreira ruiva', 'princesa que mora com os índios',
               'vira abóbora depois da meia noite', 'na país das maravilhas', 'conhecida por estar nas aventuras de peter pan',
               'seu melhor amigo é um tigre', 'mora no alto de uma torre', 'boneco de neve']
banco_palavras = ['planeta', 'meteoro', 'desenho', 'humano', 'filosofia', 'labirinto', 'serpente', 'cerveja', 'mostarda',
                  'maracuja', 'pernilongo', 'oxigenio', 'maconha', 'maracatu', 'pamonha', 'umbanda', 'democracia']
banco_dicas = ['corpo celeste', 'resíduo de explosões planetárias', 'retrato feito a mão',
               'homo sapiens', 'ciência mãe das ciências', 'fácil de entrar, difícil de sair', 'réptil de sangue frio',
               'bebida fermentada', 'molho gourmet', 'passiflora', 'inseto hematófago', 'essencial à vida',
               'erva medicinal', 'estilo muscial nordestino', 'doce de milho', 'crença africana', 'voto popular']
cont = 0
acertos = []
digitadas = []
erros = pontos = 0
dica = ''
escolhida = []
ind = random.randint(0, len(banco_palavras)-1)
while True:
    print('-'*20)
    print(' - Jogo da Forca -')
    print('-'*20)
    print(emoji.emojize('[1] :point_right: Fácil', use_aliases=True))
    print(emoji.emojize('[2] :point_right: Difícil', use_aliases=True))
    print(emoji.emojize('[3] :point_right: Maria Beatriz', use_aliases=True))
    print(emoji.emojize('[4] :point_right: Sair', use_aliases=True))
    print('-'*20)
    option = int(input('\033[31;1m - Escolha uma opção : \033[m'))
    print('-'*20)
    if option >= 1:
        if option == 4:
            print(' - Obrigado Por jogar - Volte Sempre !!')
            break
        else:
            if option == 3:
                escolhida.append(maria_beatriz[ind])
                if maria_beatriz[ind] in escolhida:
                    ind = random.randint(0,16)
                palavra_secreta = maria_beatriz[ind]
                dica = maria_dicas[ind]

            else:
                palavra_secreta = banco_palavras[ind]
                dica = banco_dicas[ind]
        while True:
            print(f'\033[36;1m PONTOS : {round(pontos, 2)}')
            senha = ''
            cont = 0
            for letra in palavra_secreta:
                senha += letra if letra in acertos else "*"
                if letra in acertos:
                    cont += 1
            print('-'*20)
            if option == 1 or option == 3:
                print(f'\033[36;1m Dica : {dica}\033[m')
                print('-'*20)
            if len(digitadas) > 0:
                print(f'Letras Digitadas :\033[32;1m {sorted(digitadas, reverse=True)}\033[m')
            print(emoji.emojize(f'\033[92;1m:point_right:  {senha.upper()}  :point_left:', use_aliases=True))
            print(emoji.emojize(f':point_right: Total  {len(senha)} letras / Letras Restantes: {len(senha) - cont}', use_aliases=True))
            print()
            if senha == palavra_secreta:
                print(f'\033[32;1mVocê Acertou a Palavra : \033[34;1m{senha.upper()} !!')
                sleep(1)
                print(emoji.emojize(':boom: :trophy: Parabéns :smile: :fire:', use_aliases=True))
                if erros == 0:
                    print(' - voCê nãO erRou neNhUma !\033[32;1m - PERFECT - ')
                    pontos += 2
                sleep(1)
                if len(palavra_secreta) >= 8:
                    pontos += 3
                else:
                    pontos += 2
                if option == 2:
                    pontos = pontos + (pontos * 0.33)
                ind = random.randint(0, len(banco_palavras) - 1)
                digitadas.clear()
                acertos.clear()
                erros = 0
                senha = ''
                break
            while True:
                tentativa = input('\n\033[31;1m - Digite uma letra : \033[m').lower().strip()
                if tentativa not in '1234567890':
                    break
                else:
                    print('Digite somente letras e não números !!')

            if tentativa in digitadas:
                print(' - Você já digitou essa letra !! - ')
                continue
            else:
                digitadas.append(tentativa)
                if tentativa in palavra_secreta:
                    acertos.append(tentativa)
                else:
                    erros += 1
                    print(' - VocÊ Errou ! -')


                # bloco das informações de erro
                if erros > 0:

                    if erros == 1:
                            print(emoji.emojize('X====\nX   :skull:', use_aliases=True))
                    elif erros == 2:
                        print(emoji.emojize('X====\nX   :skull:', use_aliases=True))
                        print('X   |')
                    elif erros == 3:
                        print(emoji.emojize('X====\nX   :skull:', use_aliases=True))
                        print('X  /|')
                    elif erros == 4:
                        print(emoji.emojize('X====\nX   :skull:', use_aliases=True))
                        print('X  /|\ ')
                    elif erros == 5:
                        print(emoji.emojize('X====\nX   :skull:', use_aliases=True))
                        print('X  /|\ ')
                        print('X  / ')
                    else:
                        print(emoji.emojize('X====\nX   :skull:', use_aliases=True))
                        print('X  /|\ ')
                        print('X  / \ ')
                        sleep(1)
                        print('-'*20)
                        sleep(1)
                        print(emoji.emojize('\033[31;1m:skull: - - Você foi enforcado !- - :astonished:\033[m', use_aliases=True))
                        digitadas.clear()
                        acertos.clear()
                        senha = ''
                        erros = 0
                        ind = random.randint(0, len(banco_palavras) - 1)
                        break










