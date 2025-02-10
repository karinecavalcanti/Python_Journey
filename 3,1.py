a = eval(input())
b = eval(input())

resp = False
if len(a) <  len(b):
    for i in range(len(a)):
        if a[i] in b:
            resp = True
print(resp)