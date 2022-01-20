#Temos mais de dua condições presentes no Python.
#As coisas podem ser 'if' ou 'else' quando se tem apenas dois caminhos:
#Porém, quando se tem mais de 2 caminhos usa-se o 'elif' pode-se ter vários ou nenhum'elif' e só usa 'elif' com 'if'
nome = str(input('Digite seu nome:'))
if nome == 'Kevyn':
    print(f'Seu nome é massa demais,{nome}!')
elif nome == 'Karina' or nome == 'Maryanne' or nome ==  'Kaio' or nome == 'Luciano':
    print(f'Saiba que eu amo você, {nome}!')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}! ')