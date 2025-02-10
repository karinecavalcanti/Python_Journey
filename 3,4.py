entrada = eval(input())
n, a, b, c = entrada

def serie(n,a,b,c):
    z = 0
    for i in range(1, n+1):
        x = ((-1)**(c+i))*((1+(a*i))/(3*(b**i)))
        z+=x
    return round(z, 3)
print(serie(n,a,b,c))