vet1 = []
vet2 = []
vet3 = []

for i in range(10):
    num = int(input("Insira um número inteiro para o primeiro vetor: "))
    vet1.append(num)

for i in range(10):
    num = int(input("Insira um número inteiro para o segundo vetor: "))
    vet2.append(num)

for i in range(10):
    vet3.append(vet1[i])
    vet3.append(vet2[i])

print("Vetor intercalado resultante é", vet3)
