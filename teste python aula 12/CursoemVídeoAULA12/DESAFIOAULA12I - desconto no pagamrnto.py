v = float(input('Digite o valor do produto:R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
fp = int(input('Digite a forma de pagamento:'))
if fp == 1:
    total = v * 0.9
elif fp == 2:
    total = v * 0.95
elif fp == 3:
    total = v
    vp = total/2
    print(f'Sua compra foi parcelada em 2x e a parcela será de R${vp}.')
elif fp == 4:
    total = v * 1.2
    parcela = int(input('Digite a quantidade de parcelas:'))
    vp = total / parcela
    print(f'Sua compra foi parcelada em {parcela}x e a parcela será de R${vp}.')
else:
    total = 0
    print('A opção digitada não é válida. Tente NOVAMENTE!')
print(f'O valor do produto foi de R${v} e o preço final será de R$ {total:.2f}! ')