from __future__ import print_function

def imprimir(X, n):
    print(')', end='')
    for i in range(n):
        print('%3d ' % X[i], end='')
    print(')')


def ordSelecao(V, n):
    for i in range(n-1, 0, -1):
        for j in range(i):
            if V[j] > V[i]:
                V[j], V[i] = V[i], V[j]


def main():
    V = [4, 2, 3, 0, 9, 3, 5, 7]
    print(V, 8)
    ordSelecao(V, 8)
    imprimir(V, 8)

main()