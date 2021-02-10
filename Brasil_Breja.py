#programa de cadastros de cervejas
#neste programa o usuário poderá cadastrar, alterar e excluir informações como
#nome, quantidade, tipo  e preço das cervejas.
print("\U0001f600", "Hello World","\U0001F606")
from datetime import datetime
from emoji import emojize
print(datetime.now().ctime())
dados = dict()
cervejas = list()
print('=+='*15)
print('=+=+=+=+=+=+=+= Brejas Brasil +=+=+=+=+=+=+=')
print('=+='*15)
print('\n')
print('=+='*15)
while True: #laço para o menu de opções
    print('=+=+=+=+=+=+=+= Menu de Opções +=+=+=+=+=+=+=')
    print('=+='*15)
    print('-'*20)
    print('[ 1 ] Cadastrar Cervejas')
    print('[ 2 ] Alterar Cadastro')
    print('[ 3 ] Excluir Cadastro')
    print('[ 4 ] Mostrar Cadastro')
    print('[ 5 ] sair')
    print('-'*20)
    opc = int(input(emojize('>> escolha aqui sua opção :point_right:',use_aliases=True)))
    print('\n')
    if opc == 1: #condição para cadastro de cervejas
        continuar = ''
        while True: #laço para cadastro de cervejas
            print(emojize(':beer:- - - Cadastro de Cervejas - - - :beer:',use_aliases=True))
            dados['marca'] = str(input(emojize('Digite o nome da cerveja :point_right:',use_aliases=True))).strip().upper()
            dados['tipo'] = str(input(emojize('Digite o tipo da cerveja :point_right:',use_aliases=True))).strip().upper()
            dados['estilo'] = str(input(emojize('Digite o estilo da cerveja :point_right:',use_aliases=True))).strip().upper()
            dados['graduação'] = float(input(emojize('Digite o volume alcóolico da cerveja :point_right:',use_aliases=True)))
            dados['IBU'] = int(input(emojize('Digite o amargor da cerveja em IBU :point_right:',use_aliases=True)))
            dados['quantidade'] = int(input(emojize('Digite a quantidade em estoque da cerveja :point_right:',use_aliases=True)))
            cervejas.append(dados.copy())
            continuar = str(input(emojize('Deseja cadastrar mais um item:[S]Sim[N]Não:point_right:',use_aliases=True))).strip().upper()
            if continuar == 'N': #condição para encerrar o laço
                break
    elif opc == 4: #condição exibir cadastro
        for i in cervejas:
            for k, v in i.items():
                print(f'{k} : {v}')






    elif opc == 5: #condição para encerarr o menu de opções
        break