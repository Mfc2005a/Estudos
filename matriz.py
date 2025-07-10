matriz = []

for i in range (3):
    linha = []
    for j in range (4):
        linha.append(int(input(f'Digite o valor para a posição ({i + 1}, {j + 1}): ')))
    matriz.append (linha)

maior_elemento = matriz[0][0]
menor_elemento = matriz[0][0]
posição_maior = (0, 0)
posição_menor = (0, 0)

for i in range(3):
    for j in range(4):
        if matriz[i][j] > maior_elemento:
            maior_elemento = matriz[i][j]
            posição_maior = (i, j)
        if matriz [i][j] < menor_elemento:
            posição_menor = (i,j)

print ('Matriz inserida:')
for linha in matriz:
    print (linha)

print (f'O maior elemento é {maior_elemento} na posição {posição_maior}!')
print (f' O menor elemento é {menor_elemento} na posição {posição_menor}!')            