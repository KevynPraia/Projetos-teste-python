s = float(input('Digite seu salário:R$'))
if s <= 1250:
    print(f'Parabéns! Você recebeu um aumento de 15% e seu salário agora é:{s*1.15}.')
else:
    print((f'Parabéns! Você recebeu um aumento de 10% e seu salário será:{s*1.1:.2f}.'))