l1 = float(input('Lado 1 em cm:'))
l2 = float(input('Lado 2 em cm:'))
l3 = float(input('Lado 3 em cm:'))
if l1 + l3 > l2 and l3 + l2 >l1 and  l1 + l2 > l3:
    print(f'Os lados são respectivamente: {l1}cm, {l2}cm e {l3}cm, logo o TRIÂNGULO EXISTE!')

else:
    print(f'Os lados são respectivamente: {l1}cm, {l2}cm, {l3}cm logo o TRIÂNGULO NÃO EXISTE!')