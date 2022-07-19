quantidade = int(input("Informe quantas notas serão calculadas: "))
somatorio = 0.0  # Já que esta variável vai ser usada como um acumulador, ela deve ser inicializada como 0

for i in range(quantidade):
    somatorio += float(input("Informe a nota {}: ".format(i+1)))

print("A média das notas é {}".format(somatorio/quantidade))
