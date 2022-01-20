n1 = float(input('1º número:'))
n2 = float(input('2º número:'))
n3 = float(input('3º número:'))
maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor foi:', maior)

if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('O menor valor foi:', menor)





