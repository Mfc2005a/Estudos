nome = str(input('Informe seu nome:'))
lastname = str(input('Informe seu ultimo nome:'))

comprimento1 = len(nome)
comprimento2 = len(lastname)

print (f' o comprimento do nome é: {comprimento1}')
print (f' o comprimento do ultimo nome é: {comprimento2}')

concatenação = nome + ' ' + lastname
print (f'Seu nome comppleto é: {concatenação}')
comprimento3 = len(concatenação)
print (f'O comprimento do seu nome completo é: {comprimento3}')