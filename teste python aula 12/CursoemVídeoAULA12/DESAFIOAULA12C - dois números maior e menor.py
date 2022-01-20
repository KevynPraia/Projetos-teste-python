n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print(f'O segundo valor é maior.')
else:
    print(f'Os valores são iguais. Logo não há maior e nem menor.')
