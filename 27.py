p,s=map(int,input().split())
z=list(map(int,input().split()))
r=list(map(int,input().split()))
a=[]
c=0
for i in range(p):
    x=r[i]/z[i]
    a.append(x)
while s>=0 and len(a)>0:
    mindex=a.index(max(a))
    if s>=z[mindex]:
        c=c+r[mindex]
        s=s-z[mindex]
    z.pop(mindex)
    r.pop(mindex)
    a.pop(mindex)
print(c)
