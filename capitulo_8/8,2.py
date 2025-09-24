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
        return len(self.c)
    
    def __mul__(self,p):
        mul = []
        for i in range(len(self.c) + len(p.c) - 1):
            mul.append(0)
        
        for i in range(len(self.c)):
            for j in range(len(p.c)):
                mul[i + j] += self.c[i] * p.c[j]
                print(mul[i + j])
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
        for i in range(len(self.c)):
            avaliar += (x**i)*self.c[i]
        return avaliar
    
p = Polinomio(eval(input()))
q = Polinomio(eval(input()))
x = float(input())

print(p.avalia(x),q.avalia(x),(p+q).avalia(x),(p-q).avalia(x),(p*q).avalia(x))