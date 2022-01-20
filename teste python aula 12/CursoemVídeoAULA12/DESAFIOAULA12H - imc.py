peso = float(input('Digite seu peso em kg:'))
altura =  float(input('Digite sua altura em metros:'))
IMC = peso / (altura*altura)
if IMC < 18.5:
    print(f'Seu IMC foi de {IMC:.1f} e você está ABAIXO DO PESO.')
elif IMC < 25:
    print(f'Seu IMC foi de {IMC:.1f} e você está no PESO IDEAL.')
elif IMC < 30:
     print(f'Seu IMC foi {IMC:.1f} e você está com SOBREPESO.')
elif IMC < 40:
    print(f'Seu IMC foi {IMC:.1f} e você está com OBESIDADE.')
else:
    print(f'Seu IMC foi de {IMC:.1f} e você está com OBESIDADE MÓRBIDA.')
