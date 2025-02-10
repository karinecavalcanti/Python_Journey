entrada = eval(input())
n, m = entrada
n : list
def menor_valor(n):
    menor = n[0]
    for i in n:
        if i < menor:
            menor = i
    return menor
def m_valores(n,m):
    n_distintos = list(set(n))
    vetor = []
    for j in range(m):
        menor = menor_valor(n_distintos)
        vetor.append(menor)
        n_distintos.remove(menor)
    return vetor

print(m_valores(n,m))