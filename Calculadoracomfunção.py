def soma_de_dois_numeros(num1, num2):
    return num1 + num2
def subtração_dois_numeros(num1, num2):
    return num1 - num2
def multiplicação_dois_numeros(num1, num2):
    return num1 * num2
def divisão_dois_numeros(num1, num2):
    
    if num2 == 0:
        return num1 / num2
    return num1 / num2

def exibir_menu():

    print ('\nCalculadora simples ')
    print ('Escolha a operação desejada:')
    print ('1. Adição')
    print ('2. Subtração')
    print ('3. Multiplicação')
    print ('4. Divisão')
    print ('5. Sair')

escolha = input('Digite o número ou "S" para sair:')

while True:
    exibir_menu()

    if escolha == 'S':
        print ('Obrigado por usar a calculadora! Até mias.')
        break
    if escolha in ('1','2','3','4',):
        try:

            if escolha == '1':
                resultado = soma_de_dois_numeros
            elif escolha == '2':
                resultado = subtração_dois_numeros
            elif escolha == '3':
                resultado = multiplicação_dois_numeros
            elif escolha == '4':
                resultado = divisão_dois_numeros
            if resultado is not None:
                print (f'\nResultado; {resultado}')

        except ValueError:
            print ('\nEntrada inválida! Por favor, digite apeanas números')
        except Exception as e:
            print (f'\nOcorreu um erro inesperado: {e}')
    else: print ('\nEscolha inválida. Por favor, escolha uma operação válida (1, 2, 3, 4 ou S para sair)')

    