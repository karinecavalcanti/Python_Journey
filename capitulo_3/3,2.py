a = input()
caracter = 0
letra = 0
numero = 0
simbolo = 0
palavra = 0

caracter = len(a)

for i in range(len(a)):
    if a[i].isalpha() == True:
        letra+=1

for i in range(len(a)):
    if a[i].isnumeric() == True:
        numero+=1

simbolo = caracter - (letra + numero)

x = a.split()
palavra = len(x)

print(caracter, letra, numero, simbolo, palavra)