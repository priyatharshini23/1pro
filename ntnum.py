p=int(input())
q=list(map(int,input().split()))
t=0
for x in range(len(q)-2):
    for y in range(x+1,len(q)-1):
        for z in range(y+1,len(q)):
            if q[x]<q[y]<q[z] and x<y<z:
                t=t+1
print(t)
