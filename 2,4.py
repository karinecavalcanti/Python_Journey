n = int(input())

def digitos(n):
    dig = len(str(n))
    return dig

def inverte(n):
    inv = str(n)[::-1]
    return int(inv)

lista = [digitos(n), inverte(n)]
print(lista)