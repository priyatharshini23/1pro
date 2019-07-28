from itertools import combinations
a,b=input().split()
b=int(q)
k=[]
cam=len(a)-b
fake=combinations(a,cam)
for i in list(fake):
  kin.append("".join(i))
print(min(k))
