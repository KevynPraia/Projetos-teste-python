from random import randint
import time #Importa a biblioteca de time
print('-=-'*25)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...... HAHAHAHAHAHA')
print('-=-'*25)
n = int(input('Digite um número entre 0 e 5 e tente me vencer:'))
print('PROCESSANDO...')
time.sleep(2) #time.sleep(x) me faz esperar um tempo x para dar o próximo comando
n1 = randint(0,5) #A máquina escolherá um número aleatório entre 0 e 5


if n == n1 :
    print(f'Parabéns! Você acertou!')
else:
    print(f'Perdeu! Eu pensei no {n1} e não no {n}.')
