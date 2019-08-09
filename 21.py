p=int(input())
q=list(map(int,input().split()))
ans=int(p/2)
a=q[:ans]
r=q[ans::]
if ((sum(a)//len(a))==(sum(r)//len(r))):
    print("yes")
else:
    print("no")
