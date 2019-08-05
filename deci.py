p=input()
n=map(int,input().split())
s=[]
for i in n:
    q=bin(i)
    s.append(q)
f=sorted(s)
f.reverse()
for j in f:
    print(int(j,2))
