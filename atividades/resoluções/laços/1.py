n = int(input("Informe o valor de n: "))

print("Sequência de Fibonacci de 1 até {}".format(n))

a = 1
b = 1

if n <= 0:
    print('A sequência de Fibonacci começa no primeiro número. Digite n >= 1 para começar.')
elif n == 1:
    print(a)
elif n >= 2:
    print('{0}, {1}'.format(a, b), end='')
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(', {}'.format(b), end='')
    print()  # para imprimir uma nova linha
