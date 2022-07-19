def le_numeros(n):
    lista = []
    for i in range(n):
        num = int(input("Insira um número inteiro para o primeiro vetor: "))
        lista.append(num)

    return lista


def main():
    v1 = le_numeros(10)
    v2 = le_numeros(10)
    v3 = le_numeros(10)

    vetr = []
    for i in range(10):
        vetr.append(v1[i])
        vetr.append(v2[i])
        vetr.append(v3[i])

    print("A lista resultante é", vetr)


if __name__ == '__main__':
    main()




