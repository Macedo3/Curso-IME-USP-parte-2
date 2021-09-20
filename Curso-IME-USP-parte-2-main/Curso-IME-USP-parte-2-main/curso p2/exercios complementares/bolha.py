class ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)

        for i in range(fim - 1):
            posicao_minimo = i

        for j in range(i + 1, fim):
            if lista[j] > lista[posicao_minimo]:
                posicao_minimo = j
        
        lista[i], lista[posicao_minimo] = lista[posicao_minimo], lista[i]

    
    def bolha(self, lista):
        fim = len(lista)

        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

        