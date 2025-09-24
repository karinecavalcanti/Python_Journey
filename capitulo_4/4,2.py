a  = eval(input())
b = eval(input())

def soma_matriz(a,b):
    if len(a) != len(b):
        return "Erro!"
    else:
        c = []
        for i in range(len(a)):
            d = []
            for j in range(len(b)):
                soma = a[i][j] + b[i][j]
                d.append(soma)
            c.append(d)
        return c

print(soma_matriz(a,b))