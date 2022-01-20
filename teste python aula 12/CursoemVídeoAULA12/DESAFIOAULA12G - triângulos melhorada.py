l1 = float(input('Lado 1:'))
l2 = float(input('Lado 2:'))
l3 = float(input('Lado 3:'))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2: #if dentro de if para impor a condição de cima e alguma debaixo
    print('O triângulo EXISTE e será um triângulo', end=' ') #Esse end='' coloca o print abaixo na mesma linha onde o end='' está.
    if l1 == l2 == l3: #O python me deixa colocar os 3 ao mesmo tempo sem precisar ir ao mesmo tempo.
        print('EQUILÁTERO.') # diferente do que seria se fosse x ==  y and z == x
    elif l1 != l2 != l3 != l1:
        print('ESCALENO.')# Esse aninhamento dentro do if principal me dá a opção de aninhar outras condições como a condição original
    else:
        print('ISÓSCELES.')
else:
    print('O triângulo NÃO EXISTE.')

