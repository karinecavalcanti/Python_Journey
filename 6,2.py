dividendo = int(input())
divisor = int(input())
def divisao(dividendo, divisor, quociente=0):
    if dividendo < divisor:
        return quociente
    return divisao(dividendo - divisor, divisor, quociente + 1)

x = divisao(dividendo, divisor)
print(x)