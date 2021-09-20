def mat_multi(A, B):
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    assert num_colunas_A == num_linhas_B
    
    C = []
    for linha in range(num_linhas_A):
        #COMEÇANDO NOVA LINHA
        C.append([])
        for coluna in range(num_colunas_B):
            #ADICIONANDO NOVOS VALORES COLUNAS EM B
            C[linha].append(0)
            for k in range(num_colunas_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    return C


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[1, 2], [3, 4], [6, 7]]
    print(mat_multi(A, B))