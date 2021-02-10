pessoa = {}
galera = []
soma = média = 0
while True:
    pessoa['nome'] = str(input('Digite o nome:')).strip().upper()
    while True:
        pessoa['sexo'] = str(input('Digite o sexo:[M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Favor digitar apenas M ou F')
    pessoa['idade'] = int(input('Digite a idade:'))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    média = soma / len(galera)
    while True:
        resp = str(input('Quer continuar [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! digite apenas Sim ou Não')
    if resp == 'N':
        break

print()
print('-'*25)
print(f'A) Ao total temos {len(galera)} pessoas cadastradas')
print(f'B)A média das idades é {média:5.2f} anos')
print(f'C)As mulheres cadastradas são :')
for p in galera:
    if p['sexo'] == 'F':
        print(f' - {p["nome"]}')
print()
print('Lista das pessoas que estão com a idade acima da média')
print('-'*25)
for p in  galera:
    if p['idade'] >= média:
        print('  ', end='')
        for k, v in p.items():
            print(f' {k} = {v} ;', end='')
        print()


