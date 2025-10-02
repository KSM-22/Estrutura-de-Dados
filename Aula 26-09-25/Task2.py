while True:
    entrada = input('Digite o número inicial e o numero final(x,y): ')
    inicio, fim = (entrada.split(','))
    numeros = []
    for i in range (int(inicio), int(fim) + 1):
        if i % 2 == 0:
            numeros.append(i)
    if len(numeros) > 10000:
        continue
    else:
        print(numeros)