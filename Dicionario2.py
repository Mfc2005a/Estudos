lista = []

for _ in range(5):
    produto = {}
    produto['id'] = input('Informe o id do produto:')
    produto['nome'] = input('Informe o nome do produto:')
    produto['preço'] = input('Informe o preço do produto:')
    lista.append(produto)

    print (f'Produtos já cadastrados: {len(lista)}')

    print ()

    for o in lista:
        print (f'id: {o['id']}')
        print ('nome:', o['nome'])
        print ('preço:', o['preço'])

        print()

print ('Quantidade de produtos cadastrados atingida!')