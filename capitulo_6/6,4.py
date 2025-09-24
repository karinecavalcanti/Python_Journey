v = eval(input())
n = [v[0]]

def BuscaBinaria(v,x):
    i = 0
    j = len(n) - 1

    while i <= j:
        m = (i+j)//2
        vm = v[m]

        if vm < x:
            i = m+1
        elif vm > x:
            j = m-1
        else: 
            return m
    return i
for z in v[1:]:
    j = len(n) - 1
    pos = BuscaBinaria(n, z)
    n.insert(pos, z)
print(n)