a = float(input("Informe a primeira nota parcial: "))
b = float(input("Informe a segunda nota parcial: "))

media_final = (a + b) / 2

if media_final == 10:
    print("Aprovado com Distinção")
elif media_final >= 7:
    print("Aprovado")
else:
    print("Reprovado")
