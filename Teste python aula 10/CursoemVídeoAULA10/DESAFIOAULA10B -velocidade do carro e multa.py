v = int(input('Digite a velocidade:'))
unidade = v-80
if v >= 80:
    print(f'Você foi multado! \nSua multa será de: {7*unidade} reais.')
else:
    print('Você está no limite permitido na rodovia.')