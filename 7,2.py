entrada = eval(input())
m, l = entrada

def caminho_diagonal(m):
    if i < 0 or j < 0 or i >= len(m) or j >= len(m[0]) or m[i][j] == 1:
        return False
    
    caminho = []

    i, j = 0, 0

    caminho.append((i, j))

    caminho_direita = caminho_diagonal(m, i, j + 1, caminho.copy())
    if caminho_direita:
        return caminho_direita

    # Tenta mover para baixo
    caminho_baixo = caminho_diagonal(m, i + 1, j, caminho.copy())
    if caminho_baixo:
        return caminho_baixo

    return False

def verifica_caminho_diagonal(m, l):
    caminho = caminho_diagonal(m)
    return caminho == l
            
print(caminho_diagonal(m), verifica_caminho_diagonal(m,l))