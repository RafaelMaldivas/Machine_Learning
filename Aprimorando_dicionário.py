from emoji import emojize
sala = []
aluno = {}
notas = []
while True:
    aluno.clear()
    notas.clear()
    aluno['Nome'] = str(input(emojize('Nome do aluno :point_right:',use_aliases=True))).strip().capitalize()
    while True:
        aluno['sexo'] = str(input(emojize('Sexo :point_right: [M]Masculino [F]Feminino ',use_aliases=True))).upper().strip()[0]
        if aluno['sexo'] in 'FM':
            break
    if aluno['sexo'] == 'F':
        atv = int(input(emojize('Quantas atividades a aluna participou? :point_right:',use_aliases=True)))
    else:
        atv = int(input(emojize('Quantas atividades o aluno participou? :point_right:', use_aliases=True)))
    for c in range(0, atv):
        notas.append(float(input(emojize(f'Nota da {c+1}ª atividade :point_right:',use_aliases=True))))
    aluno['Notas'] = notas[:]
    aluno['Média'] = (sum(notas)/atv)
    sala.append(aluno.copy())
    while True:
        resp = str(input(emojize(':point_right: Cadastrar outro aluno ? [S]sim [N]não :point_left:', use_aliases=True))).strip().upper()[0]
        if resp in 'SN':
            break
        print(emojize('Erro :warning: Resposta deve ser S ou N :warning:',use_aliases=True))
    if resp == 'N':
        break
print('-'*30)
print()
print('-'*30)
for k, v in enumerate(sala):
    for i in v.keys():
        print(f'{str(i):<15}', end=' ')
    print()
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-'*30)
print()
print('-'*30)
while True:
    busca = int(input('Escolha o cód do aluno o qual deseja saber os dados (999 encerra a busca)'))
    if busca == 999:
        print('-' * 30)
        print('FiM')
        break
    if busca >= len(sala):
        print(emojize('Erro :warning: Não existe este aluno no sistema :warning:', use_aliases=True))
    else:
        print(emojize(f':arrow_forward: Dados de {sala[busca]["Nome"]}  :arrow_left:', use_aliases=True))
        for i, n in enumerate(sala[busca]['Notas']):
            print(emojize(f':ballot_box_with_check: Na atividade {i+1} tirou {n}',use_aliases=True))
        if aluno['sexo'] == 'F':
            print(emojize(f'A média final da aluna é de {sala[busca]["Média"]:.1f}', use_aliases=True))
        else:
            print(emojize(f':books: A média final do aluno é de {sala[busca]["Média"]:.1f}', use_aliases=True))
        if sala[busca]['Média'] <= 5:
            print(emojize(f' {aluno["Nome"]} está :skull: REPROVADO :skull:', use_aliases=True))
        else:
            print(emojize(f' {aluno["Nome"]} está :fireworks: APROVADO :fireworks:', use_aliases=True))
    print('-'*30)
    print()

