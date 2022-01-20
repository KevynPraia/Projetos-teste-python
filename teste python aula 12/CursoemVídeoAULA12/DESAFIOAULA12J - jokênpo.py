import random
import time
print('\033[1;31m=-\033[m' * 20)
print('           JOKENPÔ')

print('Você consegue vencer a máquina? ''')
print('\033[1;31m=-\033[m' * 20)
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
itens = ('Pedra','Papel', 'Tesoura')
h = int(input('Escolha um número:'))
m = random.randint(0,2)
print('\033[2;35mJO\033[m')
time.sleep(1)
print('\033[2;32mKEN\033[m')
time.sleep(1)
print('\033[2;36mPÔ\033[m')
print('\033[7m*=\033[m'*15)
print(f'Você escolheu: {itens[h]}')
print(f'A máquina escolheu: {itens[m]}')
print('\033[7m*=\033[m'* 15)

if m == 0 and h == 1:
    print('Você GANHOU!')
elif m == 1 and h == 2:
    print('Você GANHOU!')
elif m == 2 and h == 0:
    print('Você Ganhou!')
elif h == 0 and m == 1:
    print('Você PERDEU!')
elif h == 1 and m == 2:
    print('Você PERDEU!')
elif h == 2 and m == 0:
    print('Você PERDEU!')

else:
    print('EMPATE!')


