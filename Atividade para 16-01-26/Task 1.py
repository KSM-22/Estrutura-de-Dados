class processo:
    lista = []

    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho
        self.next = None
        processo.lista.append(self)

    def __repr__(self):
        return f'{self.nome}: {self.tamanho}'

processo1 = processo('A', 5)
processo2 = processo('B', 10)
processo3 = processo('C', 15)
processo4 = processo('D', 20)

processo1.next = processo2
processo2.next = processo3
processo3.next = processo4
processo4.next = processo1


current = processo1
anterior = processo4

print(f'Lista de Processos: {processo.lista}')
while processo. lista:

    if current.tamanho <= 0:
        processo.lista = [p for p in processo.lista if p.nome != current.nome]
        if not processo.lista:
            break
        anterior.next = current.next
        current = current.next
    else:
        print(f'{current}' + ' --> ' + f'{current.tamanho - 5}')
        current.tamanho -= 5
        if current.tamanho <= 0:
            print(f'Encerrando processo: {current.nome}')
        current = current.next
        continue
    print(f'Lista de Processos: {processo.lista}')




