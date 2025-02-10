n = int(input())

def fibonacci(n, i = 0):
    if n == 0:
        fib = [0]
    else:
        fib = [0,1]
        while fib[-1] + fib[-2] <= n:
            sequencia = fib[-1] + fib[-2]
            fib.append(sequencia)
    return fib
def soma_fibonacci(n):
    soma = sum(fibonacci(n))
    return soma
print(fibonacci(n),"\n",soma_fibonacci(n))