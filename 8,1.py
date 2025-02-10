class Matriz:
    def __init__(self,n,m,v):
        self.n = n
        self.m = m
        self.v = []
        for i in range(n):
            n_vetor = []
            for j in range(m):
                n_vetor.append(v[i * m + j])
            self.v.append(n_vetor)

    def __add__(self,other):
        #self -> a e other -> b
        if self.n != other.n or self.m != other.m:
            raise ValueError
        
        soma = []
        for i in range(self.n):
            result = []
            for j in range(self.m):
                s = self.v[i][j] + other.v[i][j]
                result.append(s)
            soma.append(result)
        return Matriz(self.n, self.m, [item for sublist in soma for item in sublist])
    
    def __sub__(self,other):
        if self.n != other.n or self.m != other.m:
            raise ValueError
        
        subtracao = []
        for i in range(self.n):
            result = []
            for j in range(self.m):
                s = self.v[i][j] - other.v[i][j]
                result.append(s)
            subtracao.append(result)
        return Matriz(self.n, self.m, [item for sublist in subtracao for item in sublist])
        #não entendi esse return

    def __mul__(self,other):
        if self.m != other.n:
            raise ValueError
        mult = []
        for i in range(self.n):
            linha = []
            for j in range(other.m):
                total = 0
                for k in range(self.m):
                    total+= self.v[i][k] * other.v[k][j]
                linha.append(total)
            mult.append(linha)

        return Matriz(self.n, other.m, [item for sublist in mult for item in sublist] )
    
entrada = input()

if entrada.count('+') == 1:
    mat1, mat2 = entrada.split('+')
    operacao = '+'
elif entrada.count('-') == 1:
    mat1, mat2 = entrada.split('-')
    operacao = '-'
elif entrada.count('*') == 1:
    mat1, mat2 = entrada.split('*')
    operacao = '*'
else:
    raise ValueError("Operação inválida")

n1, m1, v1 = eval(mat1)
n2, m2, v2 = eval(mat2)
a = Matriz(n1, m1, v1)
b = Matriz(n2, m2, v2)

if operacao == "+":
    soma = a+b
    print(soma.v)
    
elif operacao == "-":
    sub = a-b
    print(sub.v)

elif operacao == "*":
    mult = a*b
    print(mult.v)
