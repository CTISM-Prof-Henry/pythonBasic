a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

maior = None
menor = None

if (a >= b) and (a >= c):
    maior = a
elif (b >= a) and (b >= c):
    maior = b
else:
    maior = c

if (a <= b) and (a <= c):
    menor = a
elif (b <= a) and (b <= c):
    menor = b
else:
    menor = c

print('maior: {0} menor: {1}'.format(maior, menor))
