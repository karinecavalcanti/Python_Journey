v = eval(input())
x = int(input())

def BuscaBinaria(v,x):
    n = len(v)
    i = 0
    j = n-1
    while i <= j:
        m = (i+j)//2
        vm = v[m]
        if vm < x:
            i = m+1
        elif vm > x:
            j = m-1
        else: 
            return m
    return -1
print(BuscaBinaria(v,x))