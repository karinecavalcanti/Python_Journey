A = eval(input())
B = eval(input())


def verifica(A,B,tamanho, i): 
    if i == tamanho :
        return False
    if A[i] == B[i]:
        return True
    return verifica(A,B,tamanho,i+1)  
def compara():
    if len(A)<len(B):
        tamanho = len(A)
    else: 
        tamanho = len(B)
    return verifica(A,B,tamanho, 0)
print(compara())