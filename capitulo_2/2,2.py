n = eval(input())
m = eval(input())

if len(n)<len(m):
    menor = len(n)
else:
    menor = len(m)

resp = False
for i in range(menor):
    if n[i] == m[i]:
        resp = True
        break
print(resp)