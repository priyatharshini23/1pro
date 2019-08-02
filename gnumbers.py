import math
p,q=map(int,input().split())
s=[]
a=list(map(int,input().split()))
for i in range(0,q):
    rin,win=map(int,input().split())
    s.append([rin,win])
for i in s:
    d=i[0]-1
    e=i[1]-1
    print(math.gcd(a[d],a[e]))
