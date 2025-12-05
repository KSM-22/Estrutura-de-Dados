entrada = input('ex:1,2,3,4,5,6,6') #Faça sua propria lista
lista = list(map(int, entrada.split(',')))
# lista = [1, 2, 5, 7, 1, 2, 4] #Lista pré definida

contagem = {}

for num in lista:
    if num in contagem:
        contagem[num] += 1
    else:
        contagem[num] = 1

repetidos = [num for num, freq in contagem.items() if freq > 1]

print(repetidos)