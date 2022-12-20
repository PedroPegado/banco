path = 'C:\\Users\\20211174010009\\Downloads\\Contas.txt'

# nome = input()
# idade = int(input())
# escola = input()
# tudo = f'{nome}/{idade}/{escola}\n'

# with open(path, 'a') as f:
#     f.write(tudo)

with open(path, 'r') as f:
    linhas = f.readlines()

lista = []
lista2 = []
cont = 0
while cont != len(linhas):
    contas = linhas[cont].split('/')
    lista.append(contas)
    cont+=1

print(linhas)
print(lista)

x = input()

cont2 = 0

while cont2 != len(lista):
    if lista[cont2][0] == x:
        idade = int(lista[cont2][1]) + 1
        idadestr = str(idade)
        lista[cont2][1] = idadestr
    cont2 += 1

cont3 = 0
for c in lista:
    lista2.append(lista[cont3][0])
    lista2.append(lista[cont3][1])
    lista2.append(lista[cont3][2])
    cont3 += 1

with open(path, 'w') as f:
    f.writelines(lista2)

print(linhas)
print(lista)
print(lista2)