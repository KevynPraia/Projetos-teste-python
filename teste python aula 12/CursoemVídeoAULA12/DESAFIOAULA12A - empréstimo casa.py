valorcasa = float(input('Digite o valor da casa:R$'))
salário = float(input('Digite seu salário:R$'))
anos = int(input('Digite em quantos anos:'))
meses = anos*12
prestação = valorcasa/meses
if prestação >= salário*0.3:
    print(f'A prestação será de R$ {prestação:.2f}. Seu pedido foi NEGADO!')
elif prestação < salário*0.3:
    print(f'A prestação será de R$ {prestação:.2f}. Seu pedido foi APROVADO! PARABÉNS!')