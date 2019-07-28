n=int(input())
p=1
while(p<=n and p*2<=n):
    p=p*2
if(p==n):
    print("0")
else:    
    print(n-p)
