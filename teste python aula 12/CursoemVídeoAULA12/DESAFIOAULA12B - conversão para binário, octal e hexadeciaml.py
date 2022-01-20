n = int(input('Digite um número inteiro:'))
print('''Escolha uma opção: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
escolha = int(input('Sua escolha:'))
if escolha == 1:
    print(f' {n} convertendo para BINÁRIO ficará {bin(n)[2:]}') #Transforma para BINÁRIO: bin(variável)
elif escolha == 2:
    print(f' {n} convertendo para OCTAL ficará {oct(n)[2:]}') #Transforma para OCTAL: oct(variável)

elif escolha == 3:
    print(f'{n} convertendo para HEXADECIMAL ficará {hex(n)[2:]}') #Transforma para HEXADECIMAL (variável)
else:
    print('A opção escolhida é invalida. Tente novamente!')