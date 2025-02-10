def matriz_menor(matriz, i, j):
    # Retorna a matriz menor, removendo a linha i e a coluna j
    return [linha[:j] + linha[j+1:] for linha in (matriz[:i] + matriz[i+1:])]

def determinante(matriz):
    if len(matriz) != len(matriz[0]):
        raise ValueError("A matriz deve ser quadrada")

    if len(matriz) == 1:
        return matriz[0][0]

    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    if len(matriz) == 3:
        a, b, c = matriz[0]
        d, e, f = matriz[1]
        g, h, i = matriz[2]
        return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    
    det = 0
    for j in range(len(matriz)):
        det += ((-1) ** j) * matriz[0][j] * determinante(matriz_menor(matriz, 0, j))
    return det