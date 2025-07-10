list = []
while True:
    informe = str(input('Informe uma palavra (/exit para parar):'))
    if informe == '/exit':
        conca = len(list)
        conca2 = ' ' .join(list) 
        print (f'resultado das palavras adicionadas: {conca2}')
        break
        
    else:

        list.append(informe)

