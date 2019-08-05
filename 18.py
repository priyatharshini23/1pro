p,q=map(int,input().split())
r=[]
t=0
for i in range(p):
    r.append(list(map(int,input().split())))   
for i in range(p):
    for j in range(q-1):
        for k in range(j+1,q+1):
            if r[i][j:k]==[1]*len(r[i][j:k]):
                 if all(r[p+i][j:k]==[1]*len(r[p+i][j:k]) for p in range(len(r[i][j:k])-1)):
                     if len(r[i][j:k])>t:
                        t=len(r[i][j:k])
if len(r)==1 and len(r[0])==1 and r[0][0]==1:
    print(1)
for i in range(t):
    print(*[1]*t)
