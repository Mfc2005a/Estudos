x = 5 
print ('conteudo',x)
print ('id:', id(x))
x = 10
print ('Conteudo', x)
print ('id:', id(x))

lista = [10,20,30]
print ('Lista mutável antes das alterações:')
print ('Conteúdo:',lista)
print ('id:', id(lista))
lista.append(40)
lista[0] = 0
print ('Lista mutável depois das alterações:')
print ('Conteúdo',lista)
print ('id:', id(lista))  
    