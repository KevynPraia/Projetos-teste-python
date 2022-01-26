import random
from time import sleep

nhumano = int(input('Digite um número de 1 a 10:'))
sleep(1)
print('Processando seu número!')
sleep(1)

print(f'DEIXE-ME PENSAR EM COMO DERROTÁ-LO!')

nmaquina = random.randint(1,10)

sleep(1)



if nhumano > nmaquina:
    print(f'O número escolhido foi {nhumano} e o número escolhido pela máquina foi {nmaquina}! Que pena! Chutou ALTO!'
          f' Tente Novamente!  ')
elif nmaquina == nhumano:
    print(f'O número escolhido foi {nhumano} e o número escolhido pela máquina foi {nmaquina} Você acertou! Parabéns!'
          f'VOCÊ É MUITO BOM! TEJHA DÓ DE UMA SIMPLES MÁQUINA :(')
else:
    print(f'O número escolhido foi {nhumano} e o número escolhido pela máquina foi {nmaquina} Que pena! Chutou BAIXO!'
          f' Tente Novamente!')
