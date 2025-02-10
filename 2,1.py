n = eval(input())
m = eval(input())

a = 0
for i in range(len(n)):
    mult = n[i]*m[i]
    a += mult
print(a)