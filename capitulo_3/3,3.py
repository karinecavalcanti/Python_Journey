entrada = eval(input())
x, m, s = entrada


def codificar(x,m,s):
    codificado = ""
    for i in range(len(m)):
        nx = ord(m[i]) - ord('a')
        anda = ((nx + s) % 27)
        cod = chr(anda + ord('a'))
        codificado += cod
    return codificado


def decodificar(x,m,s):
    codificado = ""
    for i in range(len(m)):
        nx = ord(m[i]) - ord('a')
        anda = ((nx - s) % 27)
        cod = chr(anda + ord('a'))
        codificado += cod
    return codificado

x : bool
if x == True:
    print(codificar(x,m,s))
else:
    print(decodificar(x,m,s))