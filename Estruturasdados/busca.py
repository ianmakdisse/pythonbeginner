def buscabinaria(lista, alvo):
    esquerda = 0;
    direita = len(lista) - 1
    while direita >= esquerda:
        meio = int(direita + esquerda / 2)
        if lista[meio] < alvo:
            esquerda = meio + 1
        elif lista[meio] > alvo:
            direita = meio - 1
        else:
            return meio

    return -1


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alvo = 3
print(buscabinaria(lista, alvo))
