n = int(input()) #número de termos da série
x = float(input())

def arctanx(n,x):
    a = 0
    for i in range(n):
        arctan = ((-1)** i)*((x**(2*i+1))/(2*i + 1))
        a += arctan
    return a

print(arctanx(n,x))