lista = []

for i in range(5):
    produto = {
        'id'
        'nome'
        'preço'


    }       

    produto['id'] = input('Digite o id do produto:')
    produto['nome'] = input('Digite o nome do produto:')
    produto['preço'] = float(input('Digite o preço do produto:'))
    lista.append(produto)

    print ('O id do produto é:',produto['id'])
    print ('O nome do produto é:',produto['nome'])
    print ('O preço do produto é:',produto['preço'])

    print()