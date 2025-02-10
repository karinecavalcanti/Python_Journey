class Forca:
    def __init__(self,palavra):
        self.palavra = palavra
    def joga(self, letra):
        palpite = ['_'] * len(self.palavra)
        letra_usada = set() #CG
        for i in range(len(letra)):
            if len(letra[i]) > 1 or letra[i] in letra_usada:
                print("Palpite Inválido: ", letra[i])
            else:
                letra_usada.add(letra[i]) #CG
                if letra[i] in self.palavra:
                    for j in range(len(self.palavra)):
                        if self.palavra[j]==letra[i]:
                            palpite.pop(j)
                            palpite.insert(j,letra[i])
                print(' '.join(palpite))#CH
                if letra[i] not in self.palavra:
                    print(' '.join(palpite))
            if '_' not in palpite:
                print("Você ganhou")
                break
            palpite2 = set(palpite)
            intersecao = palpite2.intersection(letra_usada)
            if '_' in palpite and i == len(palavra)+len(intersecao):
                print("Você perdeu")
                break
    def __repr__(self):
        return self.palavra
        
entrada = eval(input())
palavra = entrada[0]

letra = []
for i in range(1,len(entrada)):
    letra.append(entrada[i])
#CG
forca = Forca(palavra)
forca.joga(letra)

