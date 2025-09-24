m = eval(input())

def quadrado_magico(m):
    sl = 0
    sc = 0
    sdp = 0
    sds = 0
    resp = True
    for i in range(len(m)):
        
        linha = sum(m[i]) 
        sl += linha//len(m) #soma de cada linha

        sdp += m[i][i] #soma da diagonal principal
        sds += m[-(i+1)][i] #soma diagonal secundária
       
        coluna = 0
        for j in m:
            coluna += j[i]
        sc += coluna
        nsc = int(sc/len(m))

    # print(sl,sdp,sds,nsc)

    if sl!=nsc or sl!=sdp or sl!=sds or nsc!=sdp or nsc!=sds or sdp!=sds:
        resp = False
    return resp

print(quadrado_magico(m))