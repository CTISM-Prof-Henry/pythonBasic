alunos = []

for i in range(10):
    numero = int(input("Informe o número do aluno: "))
    altura = float(input("Informe a altura do aluno: "))

    aluno = {'número': numero, 'altura': altura}

    alunos.append(aluno)

menor = alunos[0]
maior = alunos[0]
for aluno in alunos:
    if aluno['altura'] > maior['altura']:
        maior = aluno
    if aluno['altura'] < menor['altura']:
        menor = aluno


print("Aluno mais alto: Número: {0} Altura: {1}".format(maior['número'], maior['altura']))
print("Aluno mais baixo: Número: {0} Altura: {1}".format(menor['número'], menor['altura']))
