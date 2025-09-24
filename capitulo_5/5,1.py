n = eval(input())
m = eval(input())

#len(n[0]) -> coluna de n
#len(n) -> linhas de n

def multiplicacao(n,m):
    if len(n[0]) == len(m): #verifica se o n° de colunas de n é igual ao n° de linhas de m
        matriz = [] #cria uma matriz vazia
        for i in range(len(n)): #para cada linha em n
            linha = [] #cria uma lista para cada linha da nova matriz
            for j in range(len(m[0])): #para cada coluna em m
                soma = 0
                for k in range(len(n[0])):#para cada coluna de n
                    soma += n[i][k] * m[k][j] 
                linha.append(soma)
            matriz.append(linha)
        return matriz
    else:
        return "Erro!"

print(multiplicacao(n,m))
