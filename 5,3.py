matriz = eval(input())

def determinante(matriz):
    """
    Calcula o determinante de uma matriz quadrada utilizando o teorema de Laplace.
    """
    # Tamanho da matriz
    n = len(matriz)
    
    # Caso base: determinante de uma matriz 1x1 é o próprio elemento
    if n == 1:
        return matriz[0][0]
    
    # Caso base: determinante de uma matriz 2x2 é ad - bc
    if n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    # Caso base: determinante de uma matriz 3x3
    if n == 3:
        return (matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1])
                - matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0])
                + matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]))

    det = 0
    for col in range(n):
        # Calcula o complemento algébrico
        cofactor = ((-1) ** col) * matriz[0][col] * determinante(menor(matriz, 0, col))
        det += cofactor
        
    return det

def menor(matriz, i, j):
    """
    Retorna o menor de uma matriz ao remover a linha i e a coluna j.
    """
    matriz_menor = [linha[:] for linha in matriz]
    del matriz_menor[i]
    
    # Remove a coluna j de cada linha da matriz resultante
    for k in range(len(matriz_menor)):
        del matriz_menor[k][j]
    
    return matriz_menor

print(determinante(matriz))