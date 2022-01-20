import datetime
datahj = datetime.date.today()
ano = datahj.year
nascimento = int(input('Digite seu ano de nascimento:'))
idade = ano - nascimento
if idade <= 9:
    print(f'Você tem {idade} anos e concorrerá no campeonato MIRIM!')
elif idade <= 14:
    print(f'Você tem {idade} anos e concorrerá no campeonato INFANTIL!')
elif idade <= 19:
    print(f'Você tem {idade} anos e concorrerá no campeonato JÚNIOR!')
elif idade <= 25:
    print(f'Você tem {idade} anos e concorrerá no campeonato SÊNIOR!')
else:
    print(f'Você tem {idade} anos e concorrerá no campeonato MASTER!')