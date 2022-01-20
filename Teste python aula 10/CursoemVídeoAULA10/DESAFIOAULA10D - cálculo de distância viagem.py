d = int(input('Digite a quilometragem:'))
d1 = d*0.5
d2 = d*0.45
if d <= 200:
    print('Você pagará:R$',d1)
else:
    print('Você pagará:R$',d2)