p=int(input())
q=list(map(int,input().split()))
r=[1]*p
for i in range(p):
    if i==0:
        if q[i]>q[i+1]:
            r[i]=r[i]+r[i+1]
    elif i>0:
        if q[i]>q[i-1]:
            r[i]=r[i]+r[i-1]
print(sum(r))
