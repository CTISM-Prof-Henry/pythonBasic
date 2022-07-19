n = int(input("Informe o valor de n: "))

if n < 2:
    print('você precisa digitar um número maior que 2!')
else:
    primos = []

    print("Números primos entre 2 e {}:".format(n))
    # de 2 até n + 1, sendo n o número informado
    for i in range(2, n + 1):
        # de 2 até a metade do número i
        primo = True
        for j in range(2, int(round((i / 2))) + 1):
            if (i % j) == 0:
                primo = False
                break
        if primo:
            primos += [i]

    print(primos)
