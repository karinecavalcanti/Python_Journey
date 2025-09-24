m = eval(input())

def caminho_diagonal(m, i=0, j=0):
    if m[0][0] == 1:
        return False
    
    if m[i][j] == 0:
        for linha in range(len(m)):
            if m[linha] == 0:
                for coluna in range(len(m[linha])):
                    tupla = [(linha,coluna)]
                    return tupla
            
    return caminho_diagonal(m)  
print(caminho_diagonal(m))