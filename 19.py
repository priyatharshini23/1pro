p=int(input())
q=[]
r=[]
for i in range(p):
 q.append(list(map(int,input().split())))
for s in q:
    for num in s:
       r.append(num)
r.sort()
for i in r:
    print(i,end=' ')
