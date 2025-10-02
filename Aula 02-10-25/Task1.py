"""
Estrutura de Dados
Aula  02-10-25

"""
while True:
    print('1. Questão 1\n'
          '2. Questão 2\n'
          '3. Questão 3\n'
          '4. Questão 4\n')
    menu = input('Selecione a questão: ')

    if menu == '1':
        """Questão 1"""
        
        valor = int(input('Digite o valor do produto: '))
        desconto = valor * 0.10
        valor2 = valor - desconto
        print(f'O valor com desconto é {valor2:.2f}.')
        print()

    if menu == '2':
        """Questão 2"""
        N1 = int(input('Digite um número: '))
        N2 = int(input('Digite outro número: '))
        
        if N1 > N2:
            print(f'{N1} é maior que {N2}')
        elif N1 < N2:
            print(f'{N1} é menor que {N2}')
        else:
            print(f'{N1} é igual a {N2}')
        print()

    if menu == '3':
        """Questão 3"""
        
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
        print()

    if menu == '4':
        """Questão 4"""
        
        while True:
            print('1. Adicionar números manualmente')
            print('2. Usar uma lista pronta')
            print('3. Sair')
            opc = input('Você prefere adicionar os números na lista ou usar uma lista pronta: ').lower()
            if opc == '1':
                lista = []
                continuar = None
                while True:
                    if continuar == '2':
                        break
                    adicionador = int(input('adicione um número: '))
                    lista.append(adicionador)
                    print('1.Sim\n'
                          '2.Não')
        
                    if continuar != 2:
                        while True:
                            continuar = input('Você deseja continuar?')
                            if continuar == '1':
                                break
                            elif continuar == '2':
                                break
                            else:
                                print('Acho que você digitou errado, tente novamente.')
                                continue
                printarte = ['.']
                for i in lista:
                    lista.sort()
                    if lista.count(i) > 1:
                        printar = (f'{i} aparece mais de uma vez')
                        if printar == printarte[-1]:
                            pass
                        else:
                            printarte.append(f'{printar}')
        
                printarte.remove(printarte[0])
                print()
                print(lista)
                for i in printarte:
                    print(i)
        
            if opc == '2':
                lista = [1, 1, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10]
                printarte = ['.']
                for i in lista:
                    lista.sort()
                    if lista.count(i) > 1:
                        printar = (f'{i} aparece mais de uma vez')
                        if printar == printarte[-1]:
                            pass
                        else:
                            printarte.append(f'{printar}')
        
                printarte.remove(printarte[0])
                print()
                print(lista)
                for i in printarte:
                    print(i)
            if opc == '3':
                print()
                break
            print()
            lista.clear()
