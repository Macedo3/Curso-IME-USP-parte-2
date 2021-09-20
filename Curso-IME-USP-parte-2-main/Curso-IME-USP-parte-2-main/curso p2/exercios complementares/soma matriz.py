def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []
    for i in range(num_linhas):
        linha = []

        for j in range(num_colunas):
            linha.append(valor)
        
        matriz.append(linha)
    return matriz


def soma_matrizes(matriza, matrizb):
    num_linhas = len(matriza)
    num_colunas = len(matriza[0])
    matrizc = cria_matriz.matriz(num_linhas, num_colunas, 0)

    for lin in range(0, num_linhas):
        for col in range(num_colunas):
            matrizc[lin][col] = matriza[lin][col] + matrizb[lin][col]

    return matrizc


if __name__ == '__main__':
    matriza = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrizb = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

    print(soma_matrizes(matriza, matrizb))