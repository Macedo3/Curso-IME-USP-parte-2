def busca(lista, numero):
    """
    Coloque uma lista de números e o número que deseja procurar na lista.
    """
    for i in range(len(lista)):
        if lista[i] == numero:
            return i
    return False

