n = eval(input())
m = eval(input())

def multiplica(n,m):
    #for z in m:
    if len(n[0]) != len(m):
         return "Erro!"
    mult = []
    for i in range (len(n)):
        linha = []  # Cria uma nova linha para a matriz resultante
        for j in range (len(m[0])):
            tot = 0  # Inicializa o valor da posição [i][j]
            for k in range(len(n[0])):
                tot += n[i][k] * m[k][j] 
            linha.append(tot) # Adiciona o valor calculado à linha resultante
        mult.append(linha)  # Adiciona a linha resultante à nova matriz 
      
    return mult

print(multiplica(n,m))