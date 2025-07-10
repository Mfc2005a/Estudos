def teste1 (a, b):
    if a > b:
        return a
    else: 
        return b
    
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
res = teste1(num1, num2)

print (f'o maior número é: {res}')