div = set()
n = eval(input())
i = 1
j = 0

def busca(x):
    global i, div
    max = x**(1/2)

    if i > max:
        i = 1
        return div
    
    if x % i == 0:
        ndiv = x // i
        div.add(ndiv)
        div.add(x // ndiv)
        i += 1
        return busca(x)
    
    else:
        i += 1
        return busca(x)


def compara():
    global j, Intersect

    if j == 0:
        a = busca(n[j]).copy()
        div.clear()
        b = busca(n[j + 1]).copy()
        div.clear()
        print(a)
        print(b)
        Intersect = a & b
        j += 1
        return compara()
    
    elif j == len(n) - 1 and j != 0:
        return Intersect
    
    else:
        b = busca(n[j + 1]).copy()
        div.clear()
        Intersect = Intersect & b
        j += 1
        return compara()
    
print(compara())