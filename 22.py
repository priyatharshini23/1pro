r=int(input())
p=list(map(int,input().split()))[:r]
z=sum(p[0:r:2])
q=sum(p[1:r:2])
if z>q:
  print(z)
else:
  print(q)
