class Tempo:
    def __init__(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s

    def __add__(self,other):
        h = self.h + other.h 
        m = self.m + other.m
        s = self.s + other.s
        if s>=60:
            s = s%60
            m +=1
        if m>=60:
            m = m%60
            h += 1
        if h>=24:
            h = h%24
        return Tempo(h,m,s)
    
    def __sub__(self,other):
        h = self.h - other.h 
        m = self.m - other.m
        s = self.s - other.s
        if m<0:
            s += 59+m
            m = 0

        return Tempo(h,m,s)
    def __repr__(self):
        return f"{self.h}h, {self.m}m, {self.s}s"
        
def transforma(string):
    h, m, s = eval(string.strip())
    return Tempo(h, m, s)
        
entrada = input()
if '+' in entrada:
    tempo1, tempo2 = entrada.split('+')
    tempo1 = transforma(tempo1)
    tempo2 = transforma(tempo2)
    adiciona = tempo1 + tempo2
    print(adiciona)
if '-' in entrada:
    tempo1,tempo2 = entrada.split('-')
    tempo1 = transforma(tempo1)
    tempo2 = transforma(tempo2)
    subtrai = tempo1 - tempo2
    print(subtrai)




