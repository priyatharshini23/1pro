p=int(input())
q=[int(i) for i in input().split()]
xen=0
for k in range(p):
   for j in range(k):
      if q[j]<q[k]:
         xen+=q[j]
print(xen) 
