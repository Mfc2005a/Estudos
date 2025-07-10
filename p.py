print ('Bem-vindo a calculadora simples')
print ('1. Adição')
print ('2. Subtração')
print ('3. Multiplicação')
print ('4. Divisão')
print ('5. Sair')

escolha = int(input('Escolha uma das operações:'))

while True:
    try:
        if escolha == 5:
            print ('Calculadora encerrada')
            break
        
        elif escolha == 1:
            num1 = int(input('Digite o primeiro número:'))
            num2 = int(input('Digite o segundo número:'))
            print (f'O resultado da operação é: {num1 + num2}')
            dado = input('deseja continuar com a operação (s/n):')
            if dado == 'n':
                print ('calculadora encerrada!')
                break
            else: continue
        elif escolha == 2:
            num1 = int(input('Digite o primeiro número:'))
            num2 = int(input('Digite o segundo número:'))
            print (f'O resultado da operação é: {num1 - num2}')
            dado = input('deseja continuar com a operação (s/n):')
            if dado == 'n':
                print ('calculadora encerrada!')
                break
            else: continue
        elif escolha == 3:
            num1 = int(input('Digite o primeiro número:'))
            num2 = int(input('Digite o segundo número:'))
            print (f'O resultado da operação é: {num1 * num2}')
            dado = input('deseja continuar com a operação (s/n):')
            if dado == 'n':
                print ('calculadora encerrada!')
                break
            else: continue
        elif escolha == 4:
            num1 = int(input('Digite o primeiro número:'))
            num2 = int(input('Digite o segundo número:'))
            print (f'O resultado da operação é: {num1 / num2}')
            dado = input('deseja continuar com a operação (s/n):')
            if dado == 'n':
                print ('calculadora encerrada!')
                break
            else: continue
        else:
            print ('Digite uma operação valida!')
    except ValueError:
        print ('Digite uma das operações existentes')