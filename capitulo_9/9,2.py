class Polinomio:
    def __init__(self, coeficientes = []):
        self.c = coeficientes

    def __setitem__(self,grau, coeficiente):
        if grau >= len(self.c):
            for i in range(len(self.c), grau + 1):
                self.c.append(0)
        self.c[grau] = coeficiente

    def __getitem__(self,grau):
        if grau < len(self.c):
            return self.c[grau]
        return 0

    def grau(self):
        return len(self.c)-1
    
    def __mul__(self,p):
        mul = []
        for i in range(len(self.c) + len(p.c) - 1):
            mul.append(0)
        
        for i in range(len(self.c)):
            for j in range(len(p.c)):
                mul[i + j] += self.c[i] * p.c[j]
        return Polinomio(mul)

    def __add__(self,p):
        soma = []
        maior = max(len(self.c), p.grau())
        for i in range(maior):
            s = self.c[i]+p[i]
            soma.append(s)
        return Polinomio(soma)

    def __sub__(self,p):
        sub = []
        maior = max(len(self.c), p.grau())
        for i in range(maior):
            s = self.c[i]-p[i]
            sub.append(s)
        return Polinomio(sub)

    def avalia(self,x):
        avaliar = 0
        for i in range(self.grau()):
            avaliar += (x**i)*self[i]
        return avaliar
    def avalia2(self,x):
        avaliar = 0
        for i in range(1,self.grau()):
            avaliar += (x**(i-1))*self[i]
        return avaliar
    
    def derivada(self):
        derivada = [self[0],]
        if self.grau() == 0:
            derivada.append(0)
            return Polinomio(derivada)
        for i in range(1,self.grau()):
            d = self[i]*i
            derivada.append(d)
        return Polinomio(derivada)
    
    def Newton(self,x,n):
        try:
            for i in range(n):
                x = x - ((self.avalia(x))/self.derivada().avalia2(x))
            return x
        except ZeroDivisionError:
            return "Abortado"

p = Polinomio(eval(input()))
x = int(input())
n = int(input())


if p.Newton(x,n) == "Abortado":
    print("Abortado")
else:
    print((format(p.avalia(p.Newton(x,n)), '.2f'),format(p.Newton(x,n),'.2f')))