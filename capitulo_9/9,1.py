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
        #inicializando a lista com 0
        for i in range(len(self.c) + len(p.c) - 1):
            mul.append(0)
        #realizando a multiplicação
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
        for i in range(1,self.grau()):
            avaliar += (x**(i-1))*self[i]
        return avaliar
    
    def derivada(self):
        derivada = [self[0],]
        if self.grau() == 0:  #derivada de constante é 0
            derivada.append(0)
            return Polinomio(derivada)
        for i in range(1,self.grau()):
            d = self[i]*i #regra do tombo
            derivada.append(d)
        return Polinomio(derivada)

entrada = eval(input())
p, x = entrada
p = Polinomio(p)
x = int(x)
print(p.derivada().avalia(x))