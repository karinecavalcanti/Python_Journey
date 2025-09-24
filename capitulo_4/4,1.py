n = eval(input())
det = []
def matriz1(n):
    det1 = n[0]
    det.append(det1)
    return det

def matriz2(n):
    det2 = (n[0][0] * n[1][1]) - (n[0][1] * n[1][0]) 
    det.append(det2)
    return det

def matriz3(n):
    det3 = (n[0][0]*n[1][1]*n[2][2] + n[0][1]*n[1][2]*n[2][0] + n[0][2]*n[1][0]*n[2][1]) - (n[0][0]*n[1][2]*n[2][1] + n[1][0]*n[0][1]*n[2][2] + n[0][2]*n[1][1]*n[2][0])
    det.append(det3)
    return det

if len(n) == 1:
    print(matriz1(n))
if len(n) == 2:
    print(matriz2(n))
if len(n) == 3:
    print(matriz3(n))