n : list = eval(input())

def busca_menor(n, i=0, menor=0): 
    if i == len(n):
        return menor
    
    if n[i] < n[menor]:
        menor = i

    return busca_menor(n, i + 1, menor)

def reorganiza(n):
    if len(n) <= 1:
        return n
    
    menor = busca_menor(n)
    n[0], n[menor] = n[menor], n[0]

    return [n[0]] + reorganiza(n[1:])
    
print(reorganiza(n))