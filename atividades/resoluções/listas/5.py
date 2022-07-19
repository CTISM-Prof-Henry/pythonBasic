# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.

alunos = [
    {'idade': 17, 'altura': 1.7},
    {'idade': 17, 'altura': 1.72},
    {'idade': 17, 'altura': 1.55},
    {'idade': 17, 'altura': 1.71},
    {'idade': 17, 'altura': 1.54},
    {'idade': 16, 'altura': 1.66},
    {'idade': 17, 'altura': 1.69},
    {'idade': 17, 'altura': 1.73},
    {'idade': 17, 'altura': 1.57},
    {'idade': 18, 'altura': 1.69}
]

media_altura = 0
for aluno in alunos:
    media_altura += aluno['altura']

media_altura /= len(alunos)

count_alunos_abaixo = 0
for aluno in alunos:
    if (aluno['altura'] <= media_altura) and (aluno['idade'] >= 17):
        count_alunos_abaixo += 1

print("A quantidade de alunos com mais de 17 anos possuem "
      "altura inferior à média de altura dos alunos é {}".format(count_alunos_abaixo)
      )
