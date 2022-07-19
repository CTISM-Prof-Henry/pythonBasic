consoantes = []

for i in range(10):
    char = input("Insira um letra: ")

    if char not in ['a', 'e', 'i', 'o', 'u']:
        consoantes.append(char)

print("Foram lidas {0} consoantes, sendo elas: {1}".format(len(consoantes), consoantes))
