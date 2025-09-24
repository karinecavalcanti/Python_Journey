n : list = eval(input())

def pares_vetor(n, i=0, j=0):
    n_tupla = []
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i] is not n[j]:
                n_lista = [n[i], n[j]]
                n_lista.sort()
                tupla = tuple(n_lista)
                
                if tupla not in n_tupla:
                    n_tupla.append(tupla)
    pares = tuple(n_tupla)
    return pares
print(pares_vetor(n))

        