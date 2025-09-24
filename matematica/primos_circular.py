n = int(input())

def primos(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def rotacao(n):
    combinacoes = []
    n_lista = str(n)
    for i in range(len(n_lista)):
        rotacao = n_lista[i:] + n_lista[:i]
        combinacoes.append(int(rotacao))
    return combinacoes

def primoscirculares(n):
    rotacoes = rotacao(n)
    for j in rotacoes:
        if not primos(j):
            return False
    return True

def lista_primocirculares(n):
    primos_circulares = []
    for n in range(2,n):
        if primoscirculares(n):
            primos_circulares.append(n)
    return primos_circulares

print(lista_primocirculares(n))