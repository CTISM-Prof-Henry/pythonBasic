a = float(input("Informe a primeira nota parcial: "))
b = float(input("Informe a segunda nota parcial: "))

media_final = (a + b) / 2

print("Notas parciais: {0}, {1}".format(a, b))
print("Média final: {}".format(media_final))

if media_final >= 9:
    conceito = 'A'
elif media_final >= 7.5:
    conceito = 'B'
elif media_final >= 6:
    conceito = 'C'
elif media_final >= 4:
    conceito = 'D'
else:
    conceito = 'E'

print("Conceito: {}".format(conceito))

if conceito not in ['D', 'E']:
    print("Aprovado!")
else:
    print("Reprovado!")
