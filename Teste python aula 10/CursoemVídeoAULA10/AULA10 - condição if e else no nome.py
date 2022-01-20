#Temos duas condições 'if' e 'else' que são dois caminhos para seguir, se não for um é o outro!
n = (str(input('Digite seu nome:'))).strip()
n1 = n.upper()
if n1 == 'KEVYN':
    print(f'Seu nome é tão bonito. \nBom dia,{n}!')
else:
    print('Seu nome é tão sem sal.')
    print(f'Bom dia, {n}!')
