#Desenvolva um algoritmo que peça ao usuário que preencha os dados de um vetor de 5
#posições com valores reais quaisquer, desde que estejam compreendidos entre 1 e 100
#(suponha que o usuário irá respeitar o enunciado). Ao final, o algoritmo deve mostrar,
#na tela, o conteúdo de cada posição do vetor, dividido por 100.

vet = []

for i in range (5):
    posição = 'Insira o elemento da posição:' + str(i+1) + ':\n'
    item = float(input(posição))

    vet.append(item)

    
  




