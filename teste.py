import emoji
from emoji import emojize
from datetime import datetime
print("\U0001f600", "Hello World","\U0001F606")

dados = dict()
dados['nome'] = str(input(emojize('Digite o seu nome:point_right:', use_aliases=True))).strip().upper()
dados['CPF'] = int(input(emojize('Digite o CPF (só o número):point_right:',use_aliases=True)))
nasc = int(input(emojize('Digite o ano de nascimento :point_right:',use_aliases=True)))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input(emojize('Nº carteira de trabalho (0 se não tiver):point_right:',use_aliases=True)))
if dados['ctps'] != 0:
    dados['contrato'] = int(input(emojize('Ano de Contratação :point_right:',use_aliases=True)))
    dados['salário'] = float(input(emojize('Salário :point_right:',use_aliases=True)))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrato'] + 55) - datetime.now().year)
for k, v in dados.items():
    if k == 'nome':
        print(f' {k}',':',f'{v}')
    elif k == 'CPF':
        print(f' {k} : {v}')
    elif k == 'idade':
        print(f'{k} : {v} anos')
    elif k == 'contrato':
        print(f'Ano do {k} : {v}')
    elif k == 'salário':
        print(f'{k} : {v} reais')
    elif k == 'aposentadoria':
        print(f'{k} : {v} anos')

alunos = {}
alunos['nome'] = str(input('Digite o nome do aluno:'))
alunos['média'] = float(input(f'Digite a média do {alunos["nome"]}'))
for k, v in alunos.items():
    print(f'{k} é igual a {v}')
if alunos['média'] > 5:
    print('Situação é igual a aprovado')
else:
    print('Situação é igual a reprovado')

sorte = {}
ranking = []
from random import randint
from time import  sleep
from operator import itemgetter
for i in range(1, 5):
    sorte[f'jogador {i}'] = randint(1, 6)
for k, v in sorte.items():
    sleep(1)
    print(f'{k} tirou {v} no dado')
print('Ranking dos Jogadores')
sleep(1)
ranking = sorted(sorte.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(1)
    print(f'{i+1}º lugar : {v[0]} com o valor {v[1]} sorteado no dado')

print('- -'*15)
print(emojize(':beer: Pesquisa Beer :beer:',use_aliases=True))
print('- -'*15)
cervejeiro = {}
rel = []
cervejas = []
preço = []
while True:
    cervejeiro['nome'] = str(input(emojize(':beer: Digite o seu nome :point_right:',use_aliases=True))).strip().upper()
    conti = ''
    beer = 0
    while True:
            cervejas.append(str(input(emojize(':beer:Digite a sua marca favorita :point_right:',use_aliases=True))).strip().upper())
            cervejeiro['cerveja'] = cervejas[:]
            beer += 1
            cervejeiro['quantidade'] = int(
                input(f'Informe a média de LATAS/Long Neck de {cervejas[0]} que consome ao mês'))
            cervejeiro['quantidade1'] = int(input(f'Informe a média de GARRAFAS '))
            preço.append(float(input(f'Informe o preço médio com o qual vc compra lata/longNeck de {cervejas[0]} R$ :')))
            preço.append(float(input(f'Informe o preço médio com o qual vc compra GARRAFA 600ml de {cervejas[0]} R$ :')))
            cervejeiro['investe'] = (preço[0] * (cervejeiro['quantidade']) + (preço[1] * cervejeiro['quantidade1']))
            cervejeiro['total'] = beer
            rel.append(cervejeiro.copy())
            cervejas.clear()
            preço.clear()
            conti = str(input(emojize(':beer: Existe outra marca de cerveja que queira mencionar? [S]Sim [N]Não',use_aliases=True))).upper().strip()
            if conti == 'N':
                break


    print(rel)
    for x, v in cervejeiro.items():
        print(f'{x} : {v}')


