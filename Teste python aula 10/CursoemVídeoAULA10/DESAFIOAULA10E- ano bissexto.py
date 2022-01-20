import datetime #Importar datas
ano = int(input('Digite um ano ou coloque 0 para o ano atual:'))
if ano == 0:
    ano = datetime.date.today().year #Vai mostrar o ano em que a máquina está.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é BISSEXTO!')
else:
    print(f'O ano de {ano} NÃO é BISSEXTO!')
