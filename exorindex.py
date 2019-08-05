p,q=map(int,input().split())
list1=list(map(int,input().split()))
p=[]
list1.insert(0,0)
for y in range(q):
     vin=[]
     r=0
     a,b=map(int,input().split())
     for i in range(a,b+1):         
         r^=list1[i]     
     p.append(r)
for y in p:
     print(y)
