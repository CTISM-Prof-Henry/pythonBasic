vet = []

for i in range(10):
    num = int(input("Insira um número inteiro: "))
    vet.append(num)

soma_quad = 0
for num in vet:
    soma_quad += num ** 2

print("A soma dos quadrados dos elementos do vetor é", soma_quad)
