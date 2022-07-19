valor_por_hora = float(input("Informe quanto você ganha por hora: "))
horas_no_mes = int(input("Informe quantas horas você trabalha no mês: "))

salario_bruto = valor_por_hora * horas_no_mes
print("Salário bruto ${}".format(salario_bruto))

IR = 0.11 * salario_bruto
INSS = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - (IR + INSS + sindicato)

print("IR R${}".format(IR))
print("INSS R${}".format(INSS))
print("Sindicato R${}".format(sindicato))
print("Salário liquido R${}".format(salario_liquido))
