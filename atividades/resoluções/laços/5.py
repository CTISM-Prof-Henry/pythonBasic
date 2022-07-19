n = int(input("Informe o valor de n: "))
h = 0

for i in range(1, n + 1):
    h += 1./i

print("Para n = {0}, temos h = {1}".format(n, h))
