"""
Questão 1:

valor = int(input('Digite o valor do produto: '))
desconto = valor * 0.10
valor2 = valor - desconto
print(f'O valor com desconto é {valor2:.2f}.')
"""

"""      
Questão 2   
N1 = int(input('Digite um número: '))
N2 = int(input('Digite outro número: '))

if N1 > N2:
    print(f'{N1} é maior que {N2}')
elif N1 < N2:
    print(f'{N1} é menor que {N2}')
else:
    print(f'{N1} é igual a {N2}')
"""

"""
Questão 3

def avaliar_idade(idade):
    printar = None
    if idade >= 0:
        printar = 'é uma criança'
    if idade >= 12:
        printar = 'é um adolescente'
    if idade >= 18:
        printar = 'é um adulto'
    if idade > 64:
        printar = 'é um idoso'
    print(printar)
idade = int(input('Digite sua idade: '))
avaliar_idade(idade)
"""

"""Questão 4"""
lista = [1, 1, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10]
contador = 0
printarte = ['.']
for i in lista:
    if lista.count(i) > 1:
        printar = (f'{i} aparece mais de uma vez')
        if printar == printarte[-1]:
            pass
        else:
            printarte.append(f'{printar}{contador}')
        print(printarte)

