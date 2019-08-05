p,q=map(int,input().split())
r=[]
s=[]
ra=[int(m) for m in input().split() ]
for i in range(0,q):
    u,v=map(int,input().split())
    for j in range(u-1 ,v):
        s.append(ra[j])
    ma=sorted(s)
    r.append(min(s))
    del s[:]
for z in range(0,len(r)):
    print(r[z])
