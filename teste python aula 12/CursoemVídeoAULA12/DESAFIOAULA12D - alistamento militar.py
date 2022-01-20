import datetime
anonasc = int(input(f'Digite seu ano de nascimento:'))
sexo = str(input('Digite seu sexo M ou F:'))
datahoje = datetime.date.today() #Esse comando mostra a data de hoje no formato: aaaa/mm/dd
idadehj = datahoje.year - anonasc #Esse comando me mostra o ano atual: variável.year
if idadehj == 18 and sexo in 'Mm' :
  print(f'Quem nasceu em {anonasc} tem {idadehj} anos em {datahoje.year}')
  print ('Você tem que se alistar IMEDIATAMENTE.')
elif idadehj < 18 and sexo in 'Mm':
  print(f'Quem nasceu em {anonasc} tem {idadehj} anos em {datahoje.year}')
  print(f'Ainda faltam {18-idadehj} anos para o alistamento.')
  print(f'Seu alistamento será em {datahoje.year+(18-idadehj)}.')

elif idadehj > 18 and sexo in 'Mm':
  print(f'Quem nasceu em {anonasc} tem {idadehj} anos em {datahoje.year}')
  print(f'Já se passaram {idadehj-18} anos desde o alistamento.')
  print(f'Seu alistamento foi em {datahoje.year-(idadehj-18)}!')

elif sexo in 'Ff':
  print('Você não poderá se alistar as forças armadas.')

